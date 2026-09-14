#!/usr/bin/env python3
# ============================================================================
#  control_node_reto2.py  -  Equipo NPC, WRO 2026 Future Engineers (Reto 2)
# ----------------------------------------------------------------------------
#  Control del Obstacle Challenge. Adaptado de control_node.py (Reto 1):
#    - Maquina de estados, conversion LiDAR, helpers, captura de
#      rumbo por boton, mediana_sector, publicacion de comandos.
#    - Cambia la navegacion por heading/wall/esquina  ->  Siguiendo_Camino
#      (Ruta Proyectada + recorte por color + SpiderSense).
#    - SE AÑADE: suscripcion /pilares, fusion camara-LiDAR, yaw acumulado para
#      conteo de vueltas, fin de carrera hibrido (yaw>1080 + magenta).
#
# ============================================================================

import math
import time

import numpy as np

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32, Empty, String
from sensor_msgs.msg import LaserScan
from npc_interfaces.msg import NpcPose

# ============================================================
# PARAMETROS
# ============================================================

LOOP_FREQUENCY_HZ = 40.0
LOOP_PERIOD_S = 1.0 / LOOP_FREQUENCY_HZ

# --- Velocidades (m/s) ---
VELOCIDAD_RECTA = 0.3
VELOCIDAD_CURVA = 0.25
VELOCIDAD_APROXIMACION_FIN = 0.28
VELOCIDAD_RETROCESO = -0.2

# --- LiDAR ---
LIDAR_RANGO_MIN = 0.01
LIDAR_RANGO_MAX = 3.0
LIDAR_FRENTE_DEG = 270.0
FOV_MIN_LIDAR = 185.0
FOV_MAX_LIDAR = 355.0

# --- Siguiendo_Camino: Ruta Proyectada (Capa 1) ---
MED_POR_GRADO = 6.0
CAST_R        = 0.075
VENTANA_DEG   = 25.0
PREC          = int(VENTANA_DEG * MED_POR_GRADO)   # 150
SKIP2         = 2
ABANICO_DEG   = 60.0       # tope fisico: ninguna candidata fuera de +/-60
# Ancho de la ventana permitida A PARTIR del pilar cuando hay recorte por color.
# Rojo: ventana = [ang_pilar, ang_pilar + ANCHO]. Verde: [ang_pilar - ANCHO,
# ang_pilar]. Siempre acotada por ABANICO_DEG. Estrecharla limita cuanto puede
# alejarse del pilar durante la evasion (evita irse a la esquina opuesta).
ANCHO_ABANICO_PILAR = 60.0
PASO_DEG      = 2.0
PESO_RUMBO    = 0.0015     # peso del desvio del rumbo en el scoring
DIST_SAT_SCORING = 1.6     # m: profundidad se satura aqui para el scoring.
                           # Direcciones con >=1.6m libres puntuan igual en
                           # profundidad; el rumbo desempata entre ellas (evita
                           # obsesion con el hueco mas profundo / irse al borde).

# --- SpiderSense (Capa 3) ---
SPIDER_DIST    = 0.22
SPIDER_ANG_MIN = 25.0
SPIDER_ANG_MAX = 75.0
SPIDER_DIV     = 3.0

# --- Fusion camara (Etapa 4, simplificada) ---
FOV_H_CAM      = 88.0
ANCHO_IMG      = 640
CENTRO_X       = 320
ALT_MIN_EVASION = 25
ALT_MIN_FIN     = 60

# --- Conversion angulo elegido -> servo ---
SERVO_MAX = 1.0
# Referencia FIJA del mapeo a servo, INDEPENDIENTE de ABANICO_DEG. Asi se puede
# explorar el abanico (60, 70, 75...) sin que cambie la agresividad del giro:
# un angulo de +45 produce el mismo servo siempre. Angulos por encima de esta
# referencia saturan en 1.0 (el clamp los recorta), que es lo deseado.
ABANICO_SERVO_DEG = 60.0
# Mapeo no lineal angulo->servo: servo = signo*(|ang|/ABANICO_SERVO_DEG)^K_SERVO
# K_SERVO < 1 hace el giro MAS agresivo en la zona media (ej. 35 grados da
# mas servo que el lineal), sin salto brusco. K_SERVO=1.0 seria lineal.
# Ajustar en pista: mas bajo = mas agresivo; mas alto = mas suave.
K_SERVO = 0.8

# --- Latch de evasion: al perder de vista el pilar (se acerca y sale del FoV
#     de la camara), mantener el recorte con el ultimo color/angulo vistos
#     durante este tiempo, para no resetear al abanico libre a media evasion
#     (evita irse a la esquina opuesta). Se cancela si aparece un pilar nuevo.
LATCH_EVASION_S = 0.6

# --- Conteo de vueltas y fin de carrera ---
YAW_3_VUELTAS_DEG = 1080.0     # 3 vueltas (referencia)
YAW_FIN_UMBRAL_DEG = 990.0     # llave de seguridad para el fin de carrera
# Parada por distancia frontal (como Reto 1)
SECTOR_FRONTAL = (-5.0, 5.0)
UMBRAL_INICIO_FRENADO = 2.0
DIST_OBJETIVO_MIN = 1.2
DIST_OBJETIVO_MAX = 1.5
TIEMPO_CONFIRMACION_PARADA_S = 0.2


# ============================================================
# CLASE PRINCIPAL
# ============================================================

class ControlNodeReto2(Node):

    def __init__(self):
        super().__init__('control_node_reto2')

        # --- Estado de sensores ---
        self.lidar = None
        self.lidar_ranges_np = None
        self.pose = None
        self.start_received = False

        # --- Estado de navegacion ---
        self.estado = 'BOOT'
        self.section_angle = 0.0       # rumbo objetivo absoluto (theta normalizado)
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0

        # --- Yaw acumulado (conteo de vueltas) ---
        self.yaw_acumulado = 0.0       # grados, des-normalizado
        self.theta_anterior = None     # para detectar saltos de +pi/-pi

        # --- Camara / fusion ---
        self.pilares_str = ""          # ultimo String de /pilares

        # --- Fin de carrera ---
        self.tiempo_inicio_banda_parada = None

        # --- Latch de evasion (recordar el ultimo pilar tras perderlo) ---
        self.latch_color = None        # 'R'/'G' del ultimo pilar visto
        self.latch_ang = 0.0           # su ultimo angulo visto
        self.latch_t = None            # instante (time.time) del ultimo avistaje

        # --- Diagnostico ---
        self._diag_contador = 0

        # --- Publicadores / Suscriptores ---
        self.pub_motor = self.create_publisher(Float32, '/cmd_motor', 10)
        self.pub_servo = self.create_publisher(Float32, '/cmd_servo', 10)

        self.create_subscription(LaserScan, '/scan', self._callback_lidar, 10)
        self.create_subscription(NpcPose, '/npcpos', self._callback_pose, 10)
        self.create_subscription(Empty, '/start', self._callback_start, 10)
        self.create_subscription(String, '/pilares', self._callback_pilares, 10)

        self.create_timer(LOOP_PERIOD_S, self.main_loop)
        self.get_logger().info('control_node_reto2 iniciado. Esperando datos...')

    # ==========================================================
    # CALLBACKS
    # ==========================================================

    def _callback_lidar(self, msg: LaserScan):
        self.lidar = msg
        ranges = np.array(msg.ranges)
        ranges[(ranges < LIDAR_RANGO_MIN) | (ranges > LIDAR_RANGO_MAX)] = np.nan
        # Rellenar nan SOLO dentro del FoV util (193-350 lidar). Un nan ahi es
        # ruido (deberia haber medida), asi que se sustituye por el vecino
        # valido mas cercano para que el marching no lo lea como "libre".
        # Fuera del FoV (chasis bloquea) se deja nan -> tratado como RANGO_MAX.
        self.lidar_ranges_np = self._rellenar_nan_en_fov(ranges, msg)

    def _rellenar_nan_en_fov(self, ranges, msg):
        n = len(ranges)
        inc = msg.angle_increment
        amin = msg.angle_min
        # indices del FoV util
        i_lo = int((math.radians(FOV_MIN_LIDAR) - amin) / inc) % n
        i_hi = int((math.radians(FOV_MAX_LIDAR) - amin) / inc) % n
        if i_lo > i_hi:
            i_lo, i_hi = i_hi, i_lo
        seg = ranges[i_lo:i_hi + 1]
        # interpolar nan con vecinos validos (relleno simple por arrastre)
        idx_validos = np.where(~np.isnan(seg))[0]
        if len(idx_validos) >= 2:
            todos = np.arange(len(seg))
            seg = np.interp(todos, idx_validos, seg[idx_validos])
            ranges[i_lo:i_hi + 1] = seg
        return ranges

    def _callback_pose(self, msg: NpcPose):
        self.pose = msg

    def _callback_start(self, msg: Empty):
        self.start_received = True
        self.get_logger().info('Senal /start recibida')

    def _callback_pilares(self, msg: String):
        self.pilares_str = msg.data

    # ==========================================================
    # HELPERS LIDAR
    # ==========================================================

    def _angulo_robot_a_indice_lidar(self, angulo_robot_deg):
        """Convencion congelada: lidar = (270 + robot) % 360 (SUMA).
        Usa angle_min/angle_increment REALES del mensaje (como Reto 1)."""
        angulo_lidar_deg = (LIDAR_FRENTE_DEG + angulo_robot_deg) % 360.0
        angulo_lidar_rad = math.radians(angulo_lidar_deg)
        indice = int(
            (angulo_lidar_rad - self.lidar.angle_min)
            / self.lidar.angle_increment
        )
        return indice % len(self.lidar.ranges)

    def _indice_a_angulo_lidar_deg(self, i):
        """Indice -> angulo LiDAR en grados, usando los datos reales del mensaje."""
        ang_rad = self.lidar.angle_min + (i % len(self.lidar.ranges)) * self.lidar.angle_increment
        return math.degrees(ang_rad) % 360.0

    def _prec_dinamico(self):
        """Cuantos indices equivalen a VENTANA_DEG, usando angle_increment real.
        Asi la ventana del marching cubre VENTANA_DEG verdaderos sea cual sea
        la densidad real del LiDAR (no depende del supuesto de 6 med/grado)."""
        inc_deg = abs(math.degrees(self.lidar.angle_increment))
        if inc_deg <= 1e-6:
            return PREC                      # fallback al valor fijo
        return max(1, int(round(VENTANA_DEG / inc_deg)))

    def _dist_robot(self, angulo_robot_deg):
        """Distancia (m) a un angulo robot, o RANGO_MAX si invalida."""
        if self.lidar_ranges_np is None:
            return LIDAR_RANGO_MAX
        i = self._angulo_robot_a_indice_lidar(angulo_robot_deg)
        d = self.lidar_ranges_np[i]
        if d is None or (isinstance(d, float) and math.isnan(d)):
            return LIDAR_RANGO_MAX
        if d <= 0.0 or d > LIDAR_RANGO_MAX:
            return LIDAR_RANGO_MAX
        return float(d)

    def _mediana_sector(self, ang_min_deg, ang_max_deg):
        """Mediana de distancias en un sector (convencion robot)."""
        if self.lidar_ranges_np is None:
            return float('inf')
        i_min = self._angulo_robot_a_indice_lidar(ang_min_deg)
        i_max = self._angulo_robot_a_indice_lidar(ang_max_deg)
        if i_min <= i_max:
            sector = self.lidar_ranges_np[i_min:i_max + 1]
        else:
            sector = np.concatenate([self.lidar_ranges_np[i_min:],
                                     self.lidar_ranges_np[:i_max + 1]])
        valido = sector[~np.isnan(sector)]
        if len(valido) == 0:
            return float('inf')
        return float(np.median(valido))

    # ==========================================================
    # HELPERS MATEMATICOS
    # ==========================================================

    @staticmethod
    def _norm_ang(a):
        while a > math.pi:
            a -= 2 * math.pi
        while a < -math.pi:
            a += 2 * math.pi
        return a

    @staticmethod
    def _clamp(v, lo, hi):
        return max(lo, min(hi, v))

    @staticmethod
    def _remap(v, in_min, in_max, out_min, out_max):
        if in_max == in_min:
            return out_min
        r = (v - in_min) / (in_max - in_min)
        return out_min + r * (out_max - out_min)

    @staticmethod
    def _angulo_a_servo(ang_deg):
        """Mapeo NO lineal angulo->servo. Preserva el signo y aplica una
        curva de potencia K_SERVO sobre la magnitud normalizada:
            servo = signo * (|ang|/ABANICO_SERVO_DEG)^K_SERVO
        Con K_SERVO<1 el giro es mas agresivo en la zona media (un angulo
        de 35 grados produce mas servo que el lineal) pero sin salto brusco:
        en 0 da 0 y en ABANICO_SERVO_DEG da 1. La referencia es FIJA y no
        depende de ABANICO_DEG, para poder mover el abanico sin alterar la
        agresividad del giro. Ajuste: K_SERVO."""
        signo = 1.0 if ang_deg >= 0 else -1.0
        mag = min(abs(ang_deg) / ABANICO_SERVO_DEG, 1.0)
        return signo * (mag ** K_SERVO) * SERVO_MAX

    # ==========================================================
    # FUSION CAMARA-LIDAR (Etapa 4, simplificada)
    # ==========================================================

    def _x_a_angulo(self, x):
        return (x - CENTRO_X) / (ANCHO_IMG / 2.0) * (FOV_H_CAM / 2.0)

    def _fusionar(self):
        """Parsea /pilares -> decision de evasion + fin de carrera."""
        pilares = []
        if self.pilares_str:
            for parte in self.pilares_str.split(';'):
                parte = parte.strip()
                if not parte:
                    continue
                campos = parte.split(':')
                if len(campos) != 3:
                    continue
                color = campos[0].strip().upper()
                try:
                    x = int(campos[1]); alt = int(campos[2])
                except ValueError:
                    continue
                if color not in ('R', 'G', 'M'):
                    continue
                pilares.append({'color': color, 'x': x, 'alt': alt,
                                'ang': self._x_a_angulo(x)})

        # evasion: R/G mas cercano (mayor altura)
        cand = [p for p in pilares if p['color'] in ('R', 'G')
                and p['alt'] >= ALT_MIN_EVASION]
        evasion = None
        if cand:
            p = max(cand, key=lambda d: d['alt'])
            evasion = {'color': p['color'], 'ang': p['ang']}

        # fin: magenta grande
        magentas = [p for p in pilares if p['color'] == 'M'
                    and p['alt'] >= ALT_MIN_FIN]
        fin = bool(magentas)
        return evasion, fin

    # ==========================================================
    # SIGUIENDO_CAMINO: Ruta Proyectada (Capa 1) + recorte (Capa 2)
    # ==========================================================

    def _hitC(self, ang_cand_lidar, i_vecino, R):
        ang_vec = self._indice_a_angulo_lidar_deg(i_vecino)
        # Ignorar vecinos FUERA del FoV util: ahi el chasis bloquea y las
        # lecturas son invalidas (envenenaban el marching lateral con 0.03).
        if not (FOV_MIN_LIDAR <= ang_vec <= FOV_MAX_LIDAR):
            return None
        d_vec = self._dist_idx(i_vecino)
        if d_vec <= 0.0:
            return None
        dtheta = abs((ang_cand_lidar - ang_vec + 180.0) % 360.0 - 180.0)
        dtheta = math.radians(dtheta)
        coll_ang = R / d_vec
        if dtheta <= coll_ang:
            return d_vec
        return None

    def _dist_idx(self, i):
        n = len(self.lidar.ranges)
        d = self.lidar_ranges_np[i % n]
        if d is None or (isinstance(d, float) and math.isnan(d)):
            return LIDAR_RANGO_MAX
        if d <= 0.0 or d > LIDAR_RANGO_MAX:
            return LIDAR_RANGO_MAX
        return float(d)

    def _marching(self, i_cand, R=CAST_R):
        ang_cand = self._indice_a_angulo_lidar_deg(i_cand)
        d_obj = self._dist_idx(i_cand)
        d_min = None
        prec = self._prec_dinamico()
        # Ventana = +/-prec indices (= +/-VENTANA_DEG), recorriendo de SKIP2 en
        # SKIP2 para mirar la mitad de los puntos. Antes los limites usaban
        # prec*SKIP2 por error, duplicando la ventana a +/-50 grados.
        for i in range(i_cand - prec, i_cand + prec, SKIP2):
            hit = self._hitC(ang_cand, i, R)
            if hit is not None and (d_min is None or hit < d_min):
                d_min = hit
        if d_min is None:
            return d_obj
        return min(d_min, d_obj)

    def _ruta_proyectada(self, recorte, rumbo_obj_robot, ang_pilar=0.0):
        """
        recorte: None / 'R' (pasar por derecha del pilar) / 'G' (por izquierda)
        rumbo_obj_robot: angulo robot hacia el eje del carril (segun IMU).
        ang_pilar: angulo del pilar (camara). El recorte se ancla AQUI, no en 0,
        y la ventana permitida tiene ancho ANCHO_ABANICO_PILAR desde el pilar:
          - Rojo: [ang_pilar, ang_pilar + ANCHO]  (pasa por la derecha del pilar)
          - Verde: [ang_pilar - ANCHO, ang_pilar] (pasa por la izquierda)
          Todo acotado por ABANICO_DEG (tope fisico). Ej: pilar rojo a -15 ->
          [-15, +45]; pilar rojo a +15 -> [+15, +75] acotado a [+15, +60].
          Limitar el extremo lejano evita que, ya girado para evadir, el robot
          encuentre la esquina opuesta como ruta mas profunda y se vaya alli.
          El CAST_R del marching se encarga de la holgura real (no rozar);
          este corte solo garantiza el LADO correcto respecto al pilar.
        Devuelve angulo robot elegido (deg).
        """
        a = -ABANICO_DEG
        b = ABANICO_DEG
        if recorte == 'R':
            a = self._clamp(ang_pilar, -ABANICO_DEG, ABANICO_DEG)
            b = self._clamp(a + ANCHO_ABANICO_PILAR, -ABANICO_DEG, ABANICO_DEG)
        elif recorte == 'G':
            b = self._clamp(ang_pilar, -ABANICO_DEG, ABANICO_DEG)
            a = self._clamp(b - ANCHO_ABANICO_PILAR, -ABANICO_DEG, ABANICO_DEG)

        mejor_ang = 0.0
        mejor_score = -1e9
        ang = a
        while ang <= b + 1e-6:
            ang_lidar = (LIDAR_FRENTE_DEG + ang) % 360.0
            if FOV_MIN_LIDAR <= ang_lidar <= FOV_MAX_LIDAR:
                i = self._angulo_robot_a_indice_lidar(ang)
                d = self._marching(i)
                # saturar la profundidad: >=1.6m cuentan igual, asi el rumbo
                # decide entre direcciones "suficientemente abiertas".
                d_sat = min(d, DIST_SAT_SCORING)
                d_norm = d_sat / DIST_SAT_SCORING
                desvio = abs(ang - rumbo_obj_robot)
                score = d_norm - PESO_RUMBO * desvio
                if score > mejor_score:
                    mejor_score = score
                    mejor_ang = ang
            ang += PASO_DEG
        return mejor_ang

    # ==========================================================
    # SpiderSense (Capa 3)
    # ==========================================================

    def _spider_sense(self, ang_elegido):
        peligro_der = self._peligro_lateral(+1)
        peligro_izq = self._peligro_lateral(-1)
        if ang_elegido > 0 and peligro_der:
            return ang_elegido / SPIDER_DIV
        if ang_elegido < 0 and peligro_izq:
            return ang_elegido / SPIDER_DIV
        return ang_elegido

    def _peligro_lateral(self, signo):
        a = SPIDER_ANG_MIN
        while a <= SPIDER_ANG_MAX + 1e-6:
            ang_robot = signo * a
            ang_lidar = (LIDAR_FRENTE_DEG + ang_robot) % 360.0
            if FOV_MIN_LIDAR <= ang_lidar <= FOV_MAX_LIDAR:
                if self._dist_robot(ang_robot) < SPIDER_DIST:
                    return True
            a += 1.0
        return False

    # ==========================================================
    # YAW ACUMULADO (conteo de vueltas)
    # ==========================================================

    def _actualizar_yaw_acumulado(self):
        """Des-normaliza theta detectando saltos de +pi/-pi y acumula grados."""
        if self.pose is None:
            return
        theta = self.pose.theta
        if self.theta_anterior is None:
            self.theta_anterior = theta
            return
        delta = theta - self.theta_anterior
        # corregir salto de wrap (-pi <-> pi)
        if delta > math.pi:
            delta -= 2 * math.pi
        elif delta < -math.pi:
            delta += 2 * math.pi
        self.yaw_acumulado += math.degrees(delta)
        self.theta_anterior = theta

    # ==========================================================
    # MAQUINA DE ESTADOS
    # ==========================================================

    def main_loop(self):
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

        self._publicar_comandos()

    def _estado_boot(self):
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0
        self.get_logger().info('BOOT completado, esperando boton...')
        self.estado = 'READY'

    def _estado_ready(self):
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0
        if self.start_received:
            # Capturar rumbo REAL al apretar el boton + resetear yaw acumulado
            self.section_angle = self.pose.theta
            self.yaw_acumulado = 0.0
            self.theta_anterior = self.pose.theta
            self.get_logger().info(
                f'Boton -> RUNNING (section_angle={math.degrees(self.section_angle):.1f} deg, '
                f'yaw acumulado reseteado)')
            self.estado = 'RUNNING'

    def _estado_running(self):
        # 1) Acumular yaw para conteo de vueltas
        self._actualizar_yaw_acumulado()

        # 2) Fusion camara: color del pilar relevante + fin de carrera
        evasion, fin_magenta = self._fusionar()

        # 3) Determinar recorte por color + angulo del pilar, con LATCH.
        #    Si veo pilar: recorto y actualizo el latch (color, angulo, tiempo).
        #    Si NO veo pilar pero lo perdi hace < LATCH_EVASION_S: sigo recortando
        #    con el ultimo color/angulo (evita resetear a media evasion).
        #    Si expiro: abanico libre.
        ahora = time.time()
        if evasion is not None:
            recorte = evasion['color']
            ang_pilar = evasion['ang']
            self.latch_color = recorte      # refrescar latch
            self.latch_ang = ang_pilar
            self.latch_t = ahora
        elif (self.latch_color is not None and self.latch_t is not None
              and (ahora - self.latch_t) < LATCH_EVASION_S):
            recorte = self.latch_color      # mantener evasion recordada
            ang_pilar = self.latch_ang
        else:
            recorte = None                  # latch expirado -> abanico libre
            ang_pilar = 0.0
            self.latch_color = None

        # 4) Rumbo objetivo en convencion robot:
        #    cuanto debo girar para alinearme con section_angle.
        #    error theta-section ya da el signo correcto (ver Reto 1).
        #    Lo pasamos a "angulo robot objetivo" (positivo=derecha).
        error_rumbo = self._norm_ang(self.pose.theta - self.section_angle)
        rumbo_obj_robot = math.degrees(error_rumbo)
        rumbo_obj_robot = self._clamp(rumbo_obj_robot, -ABANICO_DEG, ABANICO_DEG)

        # 5) Ruta Proyectada elige direccion
        ang_elegido = self._ruta_proyectada(recorte, rumbo_obj_robot, ang_pilar)

        # 6) SpiderSense corrige si hay peligro lateral
        ang_final = self._spider_sense(ang_elegido)

        # 7) Convertir angulo elegido -> servo (directo con _remap)
        servo = self._angulo_a_servo(ang_final)
        self.cmd_steering = self._clamp(servo, -1.0, 1.0)

        # 8) Velocidad adaptativa segun cuanto gira
        self.cmd_velocity = self._calcular_velocidad(self.cmd_steering)

        # --- DIAGNOSTICO: imprime cada ~0.1 s (cada 4 ciclos a 40 Hz) ---
        self._diag_contador += 1
        if self._diag_contador >= 4:
            self._diag_contador = 0
            d_frente = self._dist_robot(0.0)
            d_izq = self._dist_robot(-45.0)
            d_der = self._dist_robot(+45.0)
            # profundidades que CALCULA el marching (lo que decide la eleccion)
            m_izq = self._marching(self._angulo_robot_a_indice_lidar(-40.0))
            m_cen = self._marching(self._angulo_robot_a_indice_lidar(0.0))
            m_der = self._marching(self._angulo_robot_a_indice_lidar(+40.0))
            rec = recorte if recorte else '-'
            self.get_logger().info(
                f"[DIAG] frente={d_frente:.2f} izq={d_izq:.2f} der={d_der:.2f} | "
                f"march(-40/0/+40)={m_izq:.2f}/{m_cen:.2f}/{m_der:.2f} | "
                f"rumbo_obj={rumbo_obj_robot:+.0f} elegido={ang_elegido:+.0f} "
                f"final={ang_final:+.0f} servo={self.cmd_steering:+.2f} | "
                f"pilar={rec} yaw={self.yaw_acumulado:.0f}")

        # 9) Fin de carrera: |yaw|>900 + magenta grande -> fase final
        #    abs() porque el yaw es negativo si el sentido de giro es CW.
        if abs(self.yaw_acumulado) > YAW_FIN_UMBRAL_DEG and fin_magenta:
            self.get_logger().info(
                f'Fin disparado: yaw={self.yaw_acumulado:.0f} + magenta '
                f'-> FINISH_APPROACH')
            self.tiempo_inicio_banda_parada = None
            self.estado = 'FINISH_APPROACH'

    def _calcular_velocidad(self, servo):
        """Mas giro -> mas lento. Interpola RECTA..CURVA segun |servo|."""
        v = self._remap(abs(servo), 0.0, 1.0, VELOCIDAD_RECTA, VELOCIDAD_CURVA)
        return self._clamp(v, VELOCIDAD_CURVA, VELOCIDAD_RECTA)

    def _estado_finish_approach(self):
        """Sigue navegando con Siguiendo_Camino pero frena por dist frontal."""
        # Navegacion sigue activa (sin recorte de color: ya no importa tras 3 vueltas)
        self._actualizar_yaw_acumulado()
        error_rumbo = self._norm_ang(self.pose.theta - self.section_angle)
        rumbo_obj_robot = self._clamp(math.degrees(error_rumbo),
                                      -ABANICO_DEG, ABANICO_DEG)
        ang_elegido = self._ruta_proyectada(None, rumbo_obj_robot)
        ang_final = self._spider_sense(ang_elegido)
        servo = self._angulo_a_servo(ang_final)
        self.cmd_steering = self._clamp(servo, -1.0, 1.0)

        # Frenado por distancia frontal (como Reto 1)
        dist_frontal = self._mediana_sector(*SECTOR_FRONTAL)
        if dist_frontal > UMBRAL_INICIO_FRENADO:
            self.cmd_velocity = VELOCIDAD_APROXIMACION_FIN
            self.tiempo_inicio_banda_parada = None
        elif dist_frontal > DIST_OBJETIVO_MAX:
            self.cmd_velocity = VELOCIDAD_CURVA
            self.tiempo_inicio_banda_parada = None
        elif dist_frontal >= DIST_OBJETIVO_MIN:
            self.cmd_velocity = 0.0
            ahora = time.time()
            if self.tiempo_inicio_banda_parada is None:
                self.tiempo_inicio_banda_parada = ahora
            elif (ahora - self.tiempo_inicio_banda_parada) >= TIEMPO_CONFIRMACION_PARADA_S:
                self.get_logger().info(f'Parada confirmada a {dist_frontal:.2f} m -> STOPPED')
                self.estado = 'STOPPED'
        else:
            self.cmd_velocity = VELOCIDAD_RETROCESO
            self.tiempo_inicio_banda_parada = None

    def _estado_stopped(self):
        self.cmd_velocity = 0.0
        self.cmd_steering = 0.0

    # ==========================================================
    # PUBLICACION
    # ==========================================================

    def _publicar_comandos(self):
        m = Float32(); m.data = float(self.cmd_velocity)
        s = Float32(); s.data = float(self.cmd_steering)
        self.pub_motor.publish(m)
        self.pub_servo.publish(s)

    def destroy_node(self):
        try:
            self.pub_motor.publish(Float32(data=0.0))
            self.pub_servo.publish(Float32(data=0.0))
        except Exception:
            pass
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = ControlNodeReto2()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
