#!/usr/bin/env python3
# ============================================================
# control_node.py
# ------------------------------------------------------------
# Nodo principal de control para el Open Challenge WRO 2026
# Equipo NPC
#
# Responsabilidades:
#   - Recibir datos del bridge (/npcpos) y del LiDAR (/scan)
#   - Implementar los 4 pilares del diseño:
#       Pilar 1: localización y conteo de giros (12 giros = 3 vueltas)
#       Pilar 2: detección sentido CW/CCW y detección de esquinas
#       Pilar 3: control de heading + wall centering + velocidad
#       Pilar 4: lógica de fin de carrera (parar a 1.2-1.5m de pared)
#   - Publicar comandos /cmd_motor y /cmd_servo a 40 Hz
#
# Máquina de estados:
#   BOOT → READY → RUNNING → FINISH_APPROACH → STOPPED
#
# Convenciones (importante para entender el código):
#   - Motor positivo = adelante (firmware del Pico ya invertido)
#   - Servo positivo = DERECHA del robot (validado físicamente)
#   - Yaw (theta) positivo = CCW = giro a la izquierda (estándar ROS 2)
#   - Sectores del LiDAR en código: positivo = DERECHA del robot
#     (consistente con servo, NO con yaw)
#   - LiDAR Clockwise: el frente del robot corresponde al ángulo 270°
#     del LiDAR. La conversión robot↔LiDAR es SUMA:
#         angulo_lidar = (270 + angulo_robot) % 360
#     (porque ambos sentidos son CW)
#
# Nota crítica: IMU usa convención CCW positivo, servo usa CW positivo.
# Por eso el cálculo de error de heading invierte el orden:
#     error = norm_ang(theta - section_angle)
# Cuando theta > section_angle (robot más a la izquierda del objetivo),
# error > 0 → str_angle > 0 → servo a la DERECHA → corrige correctamente.
# ============================================================

import math
import time

import numpy as np

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32, Empty
from sensor_msgs.msg import LaserScan
from npc_interfaces.msg import NpcPose


# ============================================================
# PARÁMETROS DEL CONTROL (todos tuneables)
# ============================================================

# --- Frecuencias ---
LOOP_FREQUENCY_HZ = 40.0
LOOP_PERIOD_S = 1.0 / LOOP_FREQUENCY_HZ

# --- Velocidades (m/s) ---
# Velocidades conservadoras para depuración inicial.
# Una vez el robot esté completamente controlado, subir progresivamente.
VELOCIDAD_RECTA = 0.4
VELOCIDAD_CURVA = 0.25
VELOCIDAD_APROXIMACION_FIN = 0.7 * VELOCIDAD_RECTA  # 0.28
VELOCIDAD_RETROCESO = -0.2

# --- Control de heading (Pilar 3 Capa 1) ---
KP_RECT = 0.48
KP_GIRO = 1.91
# Umbral para considerar el giro "terminado" (turning → False).
# Antes: 45°. Bajado a 15° porque a velocidades bajas (0.4 m/s) el
# robot pierde inercia y no completaba los 90° después de cruzar 45°.
# Con 15°, el robot sigue en modo turning (Kp_giro=1.91) hasta casi
# alinearse con el rumbo objetivo, asegurando giro completo.
UMBRAL_FIN_GIRO_RAD = math.radians(15.0)  # 0.2618

# --- Wall centering (Pilar 3 Capa 2) ---
# Sectores en convención del robot: positivo = derecha
# Ajustado al FoV real del LiDAR (visible 193°-350°)
# Originalmente (80, 82); pero (270+82)%360=352° está fuera del FoV
SECTOR_WALL_DER = (75.0, 77.0)
SECTOR_WALL_IZQ = (-77.0, -75.0)
KP_LATERAL = 1.0
UMBRAL_CORREDOR_MAX = 1.1         # suma left+right
UMBRAL_DIST_POST_GIRO = 0.4       # m desde último giro
WALL_CENTERING_MAX = 0.5          # límite del strAngle generado por Capa 2

# --- Detección de esquinas y de sentido ---
# Sectores ajustados al FoV real del LiDAR (visible 193°-350°)
SECTOR_FRONTAL = (-5.0, 5.0)
SECTOR_LATERAL_DER = (65.0, 75.0)
SECTOR_LATERAL_IZQ = (-75.0, -65.0)
UMBRAL_FRONTAL = 0.7              # m, distancia para activar detección de esquina
UMBRAL_APERTURA_LATERAL = 1.0     # m, confirmación lateral
UMBRAL_DEBOUNCE_ESPACIAL = 1.0    # m desde último giro

# Nota: el sentido de giro (CW/CCW) se detecta en la PRIMERA esquina
# mirando ambos lados laterales y eligiendo el que tenga apertura.
# Hasta entonces, sentido_giro = None y el robot avanza recto.

# --- Pilar 1: conteo de giros ---
TOTAL_GIROS_OBJETIVO = 12

# --- Pilar 4: fin de carrera ---
DIST_OBJETIVO_MIN = 1.2
DIST_OBJETIVO_MAX = 1.5
UMBRAL_INICIO_FRENADO = 2.0       # cuando dist_frontal baja de 2.0, frenamos a V_Curva
TIEMPO_CONFIRMACION_PARADA_S = 0.2

# --- LiDAR ---
LIDAR_RANGO_MIN = 0.01            # m
LIDAR_RANGO_MAX = 3.0             # m
# Convención del LiDAR (calibrada empíricamente):
# El "frente del robot" corresponde al ángulo 270° del LiDAR.
# El LiDAR escanea en sentido Clockwise (CW), por lo que la
# convención del robot (CCW positivo) requiere INVERTIR el signo
# al mapear: angulo_lidar = (LIDAR_FRENTE_DEG - angulo_robot) % 360
LIDAR_FRENTE_DEG = 270.0


# ============================================================
# CLASE PRINCIPAL
# ============================================================

class ControlNode(Node):

    def __init__(self):
        super().__init__('control_node')

        # ----- Datos sensoriales (los llenan los callbacks) -----
        self.pose = None
        self.lidar = None
        self.lidar_ranges_np = None

        # ----- Estado del nodo (máquina de estados) -----
        self.estado = 'BOOT'
        self.start_received = False

        # ----- Pilar 1: conteo de giros -----
        self.turn_count = 0
        self.turning_anterior = False  # para detectar transición T→F

        # ----- Pilar 2: detección de esquinas -----
        self.sentido_giro = None  # 'CW' o 'CCW', se detecta en la 1a esquina
        self.section_angle = 0.0  # rumbo objetivo absoluto (en theta normalizado)
        self.turning = False
        self.last_turn_pos = None  # (x, y) del último giro detectado

        # ----- Pilar 3: comandos calculados -----
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0

        # ----- Pilar 4: timer de parada -----
        self.tiempo_inicio_banda_parada = None

        # ----- Publishers -----
        self.pub_motor = self.create_publisher(Float32, '/cmd_motor', 10)
        self.pub_servo = self.create_publisher(Float32, '/cmd_servo', 10)

        # ----- Subscribers -----
        self.create_subscription(LaserScan, '/scan', self._callback_lidar, 10)
        self.create_subscription(NpcPose, '/npcpos', self._callback_pose, 10)
        self.create_subscription(Empty, '/start', self._callback_start, 10)

        # ----- Timer principal a 40 Hz -----
        self.create_timer(LOOP_PERIOD_S, self.main_loop)

        self.get_logger().info('control_node iniciado, esperando datos...')

    # ==========================================================
    # CALLBACKS (cortos, solo guardan datos)
    # ==========================================================

    def _callback_lidar(self, msg: LaserScan):
        self.lidar = msg
        # Convertir a numpy una sola vez, filtrar valores fuera de rango
        ranges = np.array(msg.ranges)
        ranges[(ranges < LIDAR_RANGO_MIN) | (ranges > LIDAR_RANGO_MAX)] = np.nan
        self.lidar_ranges_np = ranges

    def _callback_pose(self, msg: NpcPose):
        self.pose = msg

    def _callback_start(self, msg: Empty):
        self.start_received = True
        self.get_logger().info('Señal /start recibida')

    # ==========================================================
    # HELPERS DEL LIDAR
    # ==========================================================

    def _angulo_robot_a_indice_lidar(self, angulo_robot_deg):
        """
        Convierte un ángulo en convención del robot al índice del array
        de ranges del LiDAR.

        Convención de los SECTORES del robot en este código:
            0° = frente, +90° = DERECHA, -90° = IZQUIERDA, 180° = atrás
            (consistente con servo: positivo = derecha)
        Convención del LiDAR:
            Escaneo Clockwise desde 0° hasta 360°. El frente del robot
            corresponde al ángulo LIDAR_FRENTE_DEG (calibrado: 270°).

        Como ambas convenciones son CW (positivo en mismo sentido),
        la conversión es SUMA: lidar = (FRENTE + robot) % 360.
        Ejemplo: robot +90° (derecha) → (270 + 90) % 360 = 0° del LiDAR.
        """
        angulo_lidar_deg = (LIDAR_FRENTE_DEG + angulo_robot_deg) % 360.0
        angulo_lidar_rad = math.radians(angulo_lidar_deg)
        indice = int(
            (angulo_lidar_rad - self.lidar.angle_min)
            / self.lidar.angle_increment
        )
        return indice % len(self.lidar.ranges)

    def _mediana_sector(self, ang_min_deg, ang_max_deg):
        """
        Calcula la mediana de las distancias en un sector angular del robot.
        Los ángulos se pasan en convención del robot (no del LiDAR).
        """
        if self.lidar_ranges_np is None:
            return float('inf')
        i_min = self._angulo_robot_a_indice_lidar(ang_min_deg)
        i_max = self._angulo_robot_a_indice_lidar(ang_max_deg)

        # Como invertimos el signo en la conversión robot→LiDAR,
        # un sector (min, max) del robot puede mapear a (i_min, i_max)
        # donde i_min > i_max. Siempre tomamos el sector correctamente
        # ya sea continuo o con wrap-around.
        if i_min <= i_max:
            sector = self.lidar_ranges_np[i_min:i_max + 1]
        else:
            # Wrap-around: ir desde i_min hasta el final, y desde 0 hasta i_max
            sector = np.concatenate([
                self.lidar_ranges_np[i_min:],
                self.lidar_ranges_np[:i_max + 1]
            ])

        sector_valido = sector[~np.isnan(sector)]
        if len(sector_valido) == 0:
            return float('inf')
        return float(np.median(sector_valido))

    # ==========================================================
    # HELPERS MATEMÁTICOS
    # ==========================================================

    @staticmethod
    def _norm_ang(angulo):
        """Normaliza un ángulo a [-pi, +pi]."""
        while angulo > math.pi:
            angulo -= 2 * math.pi
        while angulo < -math.pi:
            angulo += 2 * math.pi
        return angulo

    @staticmethod
    def _clamp(valor, minimo, maximo):
        return max(minimo, min(maximo, valor))

    @staticmethod
    def _remap(valor, in_min, in_max, out_min, out_max):
        """Mapea linealmente un valor de un rango a otro."""
        if in_max == in_min:
            return out_min
        ratio = (valor - in_min) / (in_max - in_min)
        return out_min + ratio * (out_max - out_min)

    def _dist_desde_ultimo_giro(self):
        """Distancia euclidiana desde el último giro detectado."""
        if self.last_turn_pos is None or self.pose is None:
            return float('inf')
        dx = self.pose.x - self.last_turn_pos[0]
        dy = self.pose.y - self.last_turn_pos[1]
        return math.sqrt(dx * dx + dy * dy)

    # ==========================================================
    # MÁQUINA DE ESTADOS — main_loop
    # ==========================================================

    def main_loop(self):
        # No hacer nada hasta tener datos mínimos
        if self.pose is None or self.lidar is None:
            return

        if self.estado == 'BOOT':
            self._estado_boot()
        elif self.estado == 'READY':
            self._estado_ready()
        elif self.estado == 'RUNNING':
            self._estado_running()
        elif self.estado == 'FINISH_APPROACH':
            self._estado_finish_approach()
        elif self.estado == 'STOPPED':
            self._estado_stopped()

        # Publicar siempre lo que decidió este loop
        self._publicar_comandos()

    # ----------------------------------------------------------
    # ESTADO: BOOT
    # ----------------------------------------------------------

    def _estado_boot(self):
        """
        Datos disponibles. Inicializar estado interno y pasar a READY.
        El section_angle se captura cuando se presione el botón, no aquí,
        para que sea la orientación REAL del robot en la pista
        (independiente de dónde se cargaron los nodos).
        """
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0

        self.get_logger().info('BOOT completado, esperando botón...')
        self.estado = 'READY'

    # ----------------------------------------------------------
    # ESTADO: READY
    # ----------------------------------------------------------

    def _estado_ready(self):
        """
        Estado READY: el robot está listo pero no hace nada inteligente.
        Solo espera a que se presione el botón físico (/start).
        Esto permite arrancar los nodos en la mesa de inspección y
        colocar el robot en la pista justo antes de presionar el botón.

        Al presionar el botón se captura la orientación actual del IMU
        como rumbo objetivo inicial. Así no importa dónde estaban los
        nodos cuando arrancaron: el "rumbo de carrera" se define en el
        momento de presionar el botón, con el robot ya en posición.

        El sentido de giro NO se detecta aquí: se detecta cuando el robot
        llegue a la primera esquina y vea apertura clara en un lado.
        """
        # Mantener motor parado y servo recto
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0

        # Cuando recibimos /start, capturar rumbo actual y arrancar carrera
        if self.start_received:
            self.section_angle = self.pose.theta
            self.get_logger().info(
                f'Botón presionado → RUNNING '
                f'(section_angle inicial = {math.degrees(self.section_angle):.1f}°, '
                f'sentido se detectará en 1a esquina)'
            )
            self.estado = 'RUNNING'


    # ----------------------------------------------------------
    # ESTADO: RUNNING
    # ----------------------------------------------------------

    def _estado_running(self):
        """
        Estado principal de la carrera: aplicar los 3 pilares de control.
        Cuando se cumplen los 12 giros, transición a FINISH_APPROACH.
        """
        # Pilar 2: detectar esquina (si no estamos ya girando)
        self._detectar_esquina()

        # Pilar 3 Capa 1: control de heading
        str_heading = self._calcular_heading()

        # Pilar 3 Capa 2: wall centering (si aplica)
        str_final = self._aplicar_wall_centering(str_heading)

        # Verificar fin de giro (turning: True → False)
        self._verificar_fin_giro(str_final)

        # Pilar 3 Capa 3: velocidad adaptativa
        self.cmd_velocity = self._calcular_velocidad(str_final)
        self.cmd_steering = str_final

        # Pilar 1: contar giros y verificar fin de carrera
        self._actualizar_contador_giros()

        if self.turn_count >= TOTAL_GIROS_OBJETIVO:
            self.get_logger().info(
                f'{TOTAL_GIROS_OBJETIVO} giros completados → FINISH_APPROACH'
            )
            self.estado = 'FINISH_APPROACH'

    # ----------------------------------------------------------
    # PILAR 2: DETECCIÓN DE ESQUINAS
    # ----------------------------------------------------------

    def _detectar_esquina(self):
        """
        Detecta si hay una esquina al frente y, si pasa el debounce
        espacial y la confirmación lateral, activa el modo turning con
        el nuevo section_angle.

        Si todavía no sabemos el sentido de giro (sentido_giro is None),
        en la primera esquina se mira AMBOS lados y se elige el que tenga
        apertura clara. Eso fija sentido_giro para el resto de la carrera.
        """
        if self.turning:
            return  # ya estamos girando, no detectamos otra

        dist_frontal = self._mediana_sector(*SECTOR_FRONTAL)
        if dist_frontal > UMBRAL_FRONTAL:
            return  # pared frontal aún lejos

        # Debounce espacial: ¿avanzamos lo suficiente desde el último giro?
        # En la primera esquina last_turn_pos es None y _dist_desde_ultimo_giro
        # devuelve inf, así que esta condición siempre se cumple la primera vez.
        if self._dist_desde_ultimo_giro() < UMBRAL_DEBOUNCE_ESPACIAL:
            return

        # Determinar apertura y delta_section según el sentido
        if self.sentido_giro is None:
            # PRIMERA ESQUINA: detectar sentido mirando ambos lados
            apertura_izq = self._mediana_sector(*SECTOR_LATERAL_IZQ)
            apertura_der = self._mediana_sector(*SECTOR_LATERAL_DER)

            izq_abierta = apertura_izq > UMBRAL_APERTURA_LATERAL
            der_abierta = apertura_der > UMBRAL_APERTURA_LATERAL

            if izq_abierta and not der_abierta:
                self.sentido_giro = 'CCW'
                apertura = apertura_izq
                delta_section = +math.pi / 2
            elif der_abierta and not izq_abierta:
                self.sentido_giro = 'CW'
                apertura = apertura_der
                delta_section = -math.pi / 2
            elif izq_abierta and der_abierta:
                # Ambos lados abiertos: elige el más amplio
                if apertura_izq >= apertura_der:
                    self.sentido_giro = 'CCW'
                    apertura = apertura_izq
                    delta_section = +math.pi / 2
                else:
                    self.sentido_giro = 'CW'
                    apertura = apertura_der
                    delta_section = -math.pi / 2
            else:
                # Ningún lado abierto: no podemos decidir, esperamos al
                # siguiente loop a ver si la situación cambia
                return

            self.get_logger().info(
                f'Sentido detectado en 1a esquina: {self.sentido_giro} '
                f'(izq={apertura_izq:.2f}m, der={apertura_der:.2f}m)'
            )

        elif self.sentido_giro == 'CCW':
            apertura = self._mediana_sector(*SECTOR_LATERAL_IZQ)
            delta_section = +math.pi / 2
        else:  # 'CW'
            apertura = self._mediana_sector(*SECTOR_LATERAL_DER)
            delta_section = -math.pi / 2

        # Confirmación final de apertura
        if apertura < UMBRAL_APERTURA_LATERAL:
            return

        # Esquina confirmada → activar giro
        self.section_angle = self._norm_ang(self.section_angle + delta_section)
        self.turning = True
        self.last_turn_pos = (self.pose.x, self.pose.y)

        self.get_logger().info(
            f'Esquina detectada. Nuevo section_angle = {math.degrees(self.section_angle):.1f}°'
        )

    # ----------------------------------------------------------
    # PILAR 3 CAPA 1: HEADING (P-controller con dos ganancias)
    # ----------------------------------------------------------

    def _calcular_heading(self):
        """
        Calcula strAngle usando P-controller con dos ganancias:
          - turning=True  → Kp_giro (saturación rápida)
          - turning=False → Kp_rect (suave)

        Nota sobre el signo del error:
        El IMU (theta) usa convención CCW positivo (estándar ROS 2),
        mientras que el servo usa convención CW positivo (positivo=derecha).
        Por eso el error se calcula como (theta - section_angle) en lugar de
        (section_angle - theta): cuando theta es mayor que el objetivo,
        el robot está MÁS hacia la izquierda de lo deseado y debe corregir
        hacia la DERECHA (servo positivo).
        """
        error = self._norm_ang(self.pose.theta - self.section_angle)

        if self.turning:
            str_angle = error * KP_GIRO
        else:
            str_angle = error * KP_RECT

        return self._clamp(str_angle, -1.0, 1.0)

    def _verificar_fin_giro(self, str_final):
        """
        Detecta cuándo el error de heading baja del umbral y desactiva turning.
        El conteo se hace en _actualizar_contador_giros() detectando la
        transición True→False.

        Usa la misma fórmula de error que _calcular_heading por consistencia.
        Como solo se usa abs(error), el signo no afecta el resultado.
        """
        if not self.turning:
            return

        error = self._norm_ang(self.pose.theta - self.section_angle)
        if abs(error) < UMBRAL_FIN_GIRO_RAD:
            self.turning = False
            self.get_logger().info(
                f'Fin de giro: error = {math.degrees(error):.1f}°'
            )

    # ----------------------------------------------------------
    # PILAR 3 CAPA 2: WALL CENTERING
    # ----------------------------------------------------------

    def _aplicar_wall_centering(self, str_heading):
        """
        Aplica corrección lateral si:
          - corredor estrecho (suma de laterales < 1.1 m)
          - lejos del último giro (>0.4 m)
          - no estamos en giro activo
        Regla: gana el mayor en valor absoluto entre Capa 1 y Capa 2.
        """
        if self.turning:
            return str_heading

        # Mediana de los sectores laterales para wall centering
        dist_der = self._mediana_sector(*SECTOR_WALL_DER)
        dist_izq = self._mediana_sector(*SECTOR_WALL_IZQ)

        # Verificar condiciones de activación
        if (dist_der + dist_izq) > UMBRAL_CORREDOR_MAX:
            return str_heading  # corredor demasiado ancho
        if self._dist_desde_ultimo_giro() < UMBRAL_DIST_POST_GIRO:
            return str_heading  # muy cerca del último giro

        # Calcular corrección lateral.
        # Convención: servo positivo = derecha.
        # Si robot está más cerca de pared IZQUIERDA → dist_izq < dist_der
        # → pos = dist_der - dist_izq > 0 → str_lateral > 0
        # → servo positivo = giro a la DERECHA = aleja al robot de pared izq ✅
        pos = dist_der - dist_izq
        str_lateral = self._clamp(
            pos * KP_LATERAL,
            -WALL_CENTERING_MAX,
            WALL_CENTERING_MAX,
        )

        # Regla "gana el mayor en valor absoluto"
        if abs(str_lateral) > abs(str_heading):
            return str_lateral
        return str_heading

    # ----------------------------------------------------------
    # PILAR 3 CAPA 3: VELOCIDAD ADAPTATIVA
    # ----------------------------------------------------------

    def _calcular_velocidad(self, str_angle):
        """
        Velocidad adaptativa con dos parámetros explícitos:
          - en giro (turning=True) → VELOCIDAD_CURVA fija
          - en recta → interpolación entre VELOCIDAD_RECTA y VELOCIDAD_CURVA
        """
        if self.turning:
            return VELOCIDAD_CURVA

        velocidad = self._remap(
            abs(str_angle), 0.0, 1.0,
            VELOCIDAD_RECTA, VELOCIDAD_CURVA,
        )
        return self._clamp(velocidad, VELOCIDAD_CURVA, VELOCIDAD_RECTA)

    # ----------------------------------------------------------
    # PILAR 1: CONTEO DE GIROS
    # ----------------------------------------------------------

    def _actualizar_contador_giros(self):
        """
        Cuenta giros detectando la transición turning: True → False.
        """
        if self.turning_anterior and not self.turning:
            self.turn_count += 1
            self.get_logger().info(
                f'Giro #{self.turn_count}/{TOTAL_GIROS_OBJETIVO} completado'
            )
        self.turning_anterior = self.turning

    # ----------------------------------------------------------
    # ESTADO: FINISH_APPROACH (Pilar 4)
    # ----------------------------------------------------------

    def _estado_finish_approach(self):
        """
        Mantener heading y wall centering activos, frenar progresivamente
        según distancia a la pared frontal. Detectar parada estable.
        """
        # Heading sigue activo
        str_heading = self._calcular_heading()
        str_final = self._aplicar_wall_centering(str_heading)
        self.cmd_steering = str_final

        # Lógica de velocidad según distancia frontal
        dist_frontal = self._mediana_sector(*SECTOR_FRONTAL)

        if dist_frontal > UMBRAL_INICIO_FRENADO:
            # Zona lejana: velocidad reducida
            self.cmd_velocity = VELOCIDAD_APROXIMACION_FIN
            self.tiempo_inicio_banda_parada = None
        elif dist_frontal > DIST_OBJETIVO_MAX:
            # Zona de frenado: velocidad de curva
            self.cmd_velocity = VELOCIDAD_CURVA
            self.tiempo_inicio_banda_parada = None
        elif dist_frontal >= DIST_OBJETIVO_MIN:
            # En banda de parada
            self.cmd_velocity = 0.0
            ahora = time.time()
            if self.tiempo_inicio_banda_parada is None:
                self.tiempo_inicio_banda_parada = ahora
            elif (ahora - self.tiempo_inicio_banda_parada) >= TIEMPO_CONFIRMACION_PARADA_S:
                self.get_logger().info(
                    f'Parada confirmada a {dist_frontal:.2f} m → STOPPED'
                )
                self.estado = 'STOPPED'
        else:
            # Pasado del punto objetivo: retroceder
            self.cmd_velocity = VELOCIDAD_RETROCESO
            self.tiempo_inicio_banda_parada = None

    # ----------------------------------------------------------
    # ESTADO: STOPPED (terminal)
    # ----------------------------------------------------------

    def _estado_stopped(self):
        """Motor y servo a cero. Estado terminal."""
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0

    # ==========================================================
    # PUBLICACIÓN DE COMANDOS
    # ==========================================================

    def _publicar_comandos(self):
        msg_motor = Float32()
        msg_motor.data = float(self.cmd_velocity)
        self.pub_motor.publish(msg_motor)

        msg_servo = Float32()
        msg_servo.data = float(self.cmd_steering)
        self.pub_servo.publish(msg_servo)

    # ==========================================================
    # CIERRE LIMPIO
    # ==========================================================

    def destroy_node(self):
        """Enviar comandos cero antes de cerrar."""
        try:
            msg_motor = Float32()
            msg_motor.data = 0.0
            self.pub_motor.publish(msg_motor)

            msg_servo = Float32()
            msg_servo.data = 0.0
            self.pub_servo.publish(msg_servo)
        except Exception:
            pass
        super().destroy_node()


# ============================================================
# ENTRY POINT
# ============================================================

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        try:
            rclpy.shutdown()
        except Exception:
            pass


if __name__ == '__main__':
    main()
