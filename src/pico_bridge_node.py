#!/usr/bin/env python3
# ============================================================
# pico_bridge_node.py
# ------------------------------------------------------------
# Nodo ROS 2 que actúa como puente entre el firmware del
# Pimoroni Pico Plus 2 (vía USB serial) y el resto del sistema
# ROS 2 corriendo en la Raspberry Pi 5.
#
# Proyecto: WRO 2026 Future Engineers — Equipo NPC
# Etapa: 2 (puente Pico ↔ ROS 2)
#
# Responsabilidades:
#   1. Detectar y conectarse automáticamente a la Pico por USB
#   2. Leer continuamente líneas CSV del Pico (hilo dedicado)
#   3. Publicar en topics ROS 2:
#        /npcpos  (NpcPose)         — pose del robot
#        /imu     (sensor_msgs/Imu) — datos del IMU
#        /encoder (std_msgs/Int32)  — ticks crudos del encoder
#        /start   (std_msgs/Empty)  — botón físico presionado
#   4. Suscribirse a:
#        /cmd_motor (Float32) — velocidad en m/s para el motor
#        /cmd_servo (Float32) — steering [-1, +1] para el servo
#   5. Reenviar comandos al Pico formateados como CSV
#   6. Reconectar automáticamente si se pierde la comunicación
#
# Protocolo serial (terminador '\n'):
#   Pico → Pi5:
#     POS,x,y,theta,acc_yaw
#     IMU,yaw,qx,qy,qz
#     ENC,ticks
#     BTN                          (botón físico presionado)
#     BOOT,mensaje | OK,mensaje | ERR,mensaje
#   Pi5 → Pico:
#     M,velocidad   (ej: "M,0.80")
#     S,steering    (ej: "S,-0.25")
#     STOP
# ============================================================

import threading
import time

import rclpy
from rclpy.node import Node

# Tipos de mensajes estándar
from std_msgs.msg import Float32, Int32, Empty
from sensor_msgs.msg import Imu

# Tipo de mensaje personalizado (definido en npc_interfaces)
from npc_interfaces.msg import NpcPose

# Comunicación serial
import serial
from serial.tools import list_ports


# Configuración serial
SERIAL_BAUDRATE = 921600
SERIAL_TIMEOUT_S = 1.0
RECONNECT_DELAY_S = 2.0


class PicoBridgeNode(Node):
    """
    Nodo puente entre el Pico (USB serial) y ROS 2.
    No contiene lógica del robot, solo traduce mensajes.
    """

    def __init__(self):
        super().__init__('pico_bridge')
        self.get_logger().info('Iniciando pico_bridge_node...')

        # ----------------------------------------------------------
        # Conexión serial al Pico
        # ----------------------------------------------------------
        self.ser = None
        self.serial_lock = threading.Lock()  # protege escrituras concurrentes
        self.conectar_pico()

        # ----------------------------------------------------------
        # Publishers (de Pico hacia ROS 2)
        # ----------------------------------------------------------
        self.pub_pose = self.create_publisher(NpcPose, '/npcpos', 10)
        self.pub_imu = self.create_publisher(Imu, '/imu', 10)
        self.pub_encoder = self.create_publisher(Int32, '/encoder', 10)
        self.pub_start = self.create_publisher(Empty, '/start', 10)

        # ----------------------------------------------------------
        # Subscribers (de ROS 2 hacia Pico)
        # ----------------------------------------------------------
        self.create_subscription(Float32, '/cmd_motor', self.callback_motor, 10)
        self.create_subscription(Float32, '/cmd_servo', self.callback_servo, 10)

        # ----------------------------------------------------------
        # Hilo dedicado a leer del USB sin bloquear el nodo principal
        # ----------------------------------------------------------
        self.running = True
        self.read_thread = threading.Thread(target=self.usb_read_loop)
        self.read_thread.daemon = True  # muere cuando muere el nodo principal
        self.read_thread.start()

        self.get_logger().info('pico_bridge_node listo.')

    # ==========================================================
    # CONEXIÓN AL PICO
    # ==========================================================

    def conectar_pico(self):
        """
        Busca el puerto USB del Pico Plus 2 y abre la conexión.
        Identificación por descripción del puerto (más robusto que
        hardcoded /dev/ttyACM0).
        """
        puerto = self._encontrar_puerto_pico()
        if puerto is None:
            self.get_logger().error(
                'No se encontró el Pico. Verifica conexión USB.'
            )
            return False

        try:
            self.ser = serial.Serial(
                port=puerto,
                baudrate=SERIAL_BAUDRATE,
                timeout=SERIAL_TIMEOUT_S,
            )
            time.sleep(0.5)  # esperar a que el Pico termine de reiniciarse
            self.ser.reset_input_buffer()  # descartar basura acumulada
            self.get_logger().info(f'Conectado al Pico en {puerto}')
            return True
        except (serial.SerialException, OSError) as e:
            self.get_logger().error(f'No se pudo abrir {puerto}: {e}')
            self.ser = None
            return False

    def _encontrar_puerto_pico(self):
        """
        Recorre puertos serie disponibles y devuelve el primero que
        parezca ser una Pico (por descripción del producto).
        Si no encuentra, devuelve None.
        """
        for port in list_ports.comports():
            # La descripción puede contener "Pico", "RP2350", "Board CDC"
            # según firmware y SO. Buscamos términos típicos.
            descripcion = (port.description or '').lower()
            producto = (port.product or '').lower()

            if any(term in descripcion or term in producto
                   for term in ['pico', 'rp2350', 'rp2040', 'board cdc']):
                # Filtrar dispositivos del LiDAR (CP210x) por si acaso
                if 'cp210' not in descripcion and 'cp210' not in producto:
                    self.get_logger().info(
                        f'Pico detectado: {port.device} '
                        f'(descripción: {port.description}, producto: {port.product})'
                    )
                    return port.device

        # Fallback: probar /dev/ttyACM0 si no encontramos por descripción
        for port in list_ports.comports():
            if port.device.startswith('/dev/ttyACM'):
                self.get_logger().warn(
                    f'Pico no identificado por descripción, '
                    f'probando con {port.device}'
                )
                return port.device

        return None

    def reconectar(self):
        """Intenta reconectar el USB tras un fallo de comunicación."""
        if self.ser is not None:
            try:
                self.ser.close()
            except Exception:
                pass
            self.ser = None

        self.get_logger().warn(
            f'Intentando reconectar en {RECONNECT_DELAY_S}s...'
        )
        time.sleep(RECONNECT_DELAY_S)
        return self.conectar_pico()

    # ==========================================================
    # LOOP DE LECTURA (HILO SEPARADO)
    # ==========================================================

    def usb_read_loop(self):
        """
        Loop que corre en hilo dedicado. Lee líneas del USB y las
        parsea. Si hay error de comunicación, intenta reconectar.
        """
        while self.running and rclpy.ok():
            if self.ser is None or not self.ser.is_open:
                self.reconectar()
                continue

            try:
                linea_bytes = self.ser.readline()
                if not linea_bytes:
                    continue  # timeout, nada que leer

                linea = linea_bytes.decode('utf-8', errors='ignore').strip()
                if linea:
                    self.parsear_linea(linea)

            except (serial.SerialException, OSError) as e:
                self.get_logger().error(f'Error de USB: {e}')
                self.reconectar()
            except Exception as e:
                self.get_logger().error(f'Error inesperado en lectura: {e}')

    # ==========================================================
    # PARSER
    # ==========================================================

    def parsear_linea(self, linea):
        """
        Identifica el tipo de mensaje y delega al publicador
        correspondiente. Errores de parseo se loggean pero no
        interrumpen el flujo.
        """
        partes = linea.split(',')
        if len(partes) == 0:
            return

        tipo = partes[0]
        valores = partes[1:]

        if tipo == 'POS':
            self._publicar_pose(valores)
        elif tipo == 'IMU':
            self._publicar_imu(valores)
        elif tipo == 'ENC':
            self._publicar_encoder(valores)
        elif tipo == 'BTN':
            self._publicar_start()
        elif tipo in ('BOOT', 'OK'):
            self.get_logger().info(f'Pico: {linea}')
        elif tipo == 'ERR':
            self.get_logger().error(f'Pico: {linea}')
        else:
            self.get_logger().warn(f'Tipo desconocido: {linea}')

    def _publicar_pose(self, valores):
        """POS,x,y,theta,acc_yaw"""
        try:
            if len(valores) < 4:
                raise ValueError(f'POS necesita 4 valores, llegaron {len(valores)}')
            msg = NpcPose()
            msg.x = float(valores[0])
            msg.y = float(valores[1])
            msg.theta = float(valores[2])
            msg.acc_yaw = float(valores[3])
            self.pub_pose.publish(msg)
        except (ValueError, IndexError) as e:
            self.get_logger().warn(f'POS malformado ({e}): {valores}')

    def _publicar_imu(self, valores):
        """
        IMU,yaw,qx,qy,qz
        Publicamos en sensor_msgs/Imu llenando solo orientation.
        La componente w del cuaternión se reconstruye:
          qw = sqrt(1 - qx² - qy² - qz²)
        """
        try:
            if len(valores) < 4:
                raise ValueError(f'IMU necesita 4 valores, llegaron {len(valores)}')

            yaw = float(valores[0])  # noqa: F841 (disponible si lo necesitamos)
            qx = float(valores[1])
            qy = float(valores[2])
            qz = float(valores[3])

            # Reconstruir qw a partir de la restricción de norma unitaria
            qw_squared = 1.0 - qx * qx - qy * qy - qz * qz
            qw = (qw_squared ** 0.5) if qw_squared > 0 else 0.0

            msg = Imu()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'imu_link'
            msg.orientation.x = qx
            msg.orientation.y = qy
            msg.orientation.z = qz
            msg.orientation.w = qw
            # Marcar covarianzas no disponibles
            msg.orientation_covariance[0] = -1.0
            msg.angular_velocity_covariance[0] = -1.0
            msg.linear_acceleration_covariance[0] = -1.0
            self.pub_imu.publish(msg)
        except (ValueError, IndexError) as e:
            self.get_logger().warn(f'IMU malformado ({e}): {valores}')

    def _publicar_encoder(self, valores):
        """ENC,ticks"""
        try:
            if len(valores) < 1:
                raise ValueError('ENC necesita 1 valor')
            msg = Int32()
            msg.data = int(valores[0])
            self.pub_encoder.publish(msg)
        except (ValueError, IndexError) as e:
            self.get_logger().warn(f'ENC malformado ({e}): {valores}')

    def _publicar_start(self):
        """
        BTN — botón físico presionado en el Pico.
        Publica mensaje vacío en /start para que el control_node
        pueda transicionar de READY a RUNNING.
        """
        self.pub_start.publish(Empty())
        self.get_logger().info('Botón de arranque presionado → /start publicado')

    # ==========================================================
    # CALLBACKS (ROS 2 → PICO)
    # ==========================================================

    def callback_motor(self, msg: Float32):
        """Recibe /cmd_motor y envía 'M,valor' al Pico."""
        comando = f'M,{msg.data:.3f}\n'
        self._enviar_pico(comando)

    def callback_servo(self, msg: Float32):
        """Recibe /cmd_servo y envía 'S,valor' al Pico."""
        comando = f'S,{msg.data:.3f}\n'
        self._enviar_pico(comando)

    def _enviar_pico(self, comando: str):
        """
        Escribe un comando al Pico de forma thread-safe.
        Usa lock porque puede haber múltiples callbacks concurrentes.
        """
        if self.ser is None or not self.ser.is_open:
            self.get_logger().warn(
                f'Sin conexión, descartando comando: {comando.strip()}'
            )
            return

        try:
            with self.serial_lock:
                self.ser.write(comando.encode('utf-8'))
        except (serial.SerialException, OSError) as e:
            self.get_logger().error(f'Error escribiendo al Pico: {e}')
            # La reconexión se manejará en el hilo de lectura

    # ==========================================================
    # CIERRE LIMPIO
    # ==========================================================

    def destroy_node(self):
        """Cierra recursos limpiamente al destruir el nodo."""
        self.get_logger().info('Cerrando pico_bridge_node...')
        self.running = False

        # Enviar STOP al Pico antes de cerrar
        try:
            if self.ser is not None and self.ser.is_open:
                with self.serial_lock:
                    self.ser.write(b'STOP\n')
                    self.ser.flush()
                time.sleep(0.1)
                self.ser.close()
        except Exception as e:
            self.get_logger().warn(f'Error al cerrar serial: {e}')

        super().destroy_node()


# ==============================================================
# ENTRY POINT
# ==============================================================

def main(args=None):
    rclpy.init(args=args)
    node = PicoBridgeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
