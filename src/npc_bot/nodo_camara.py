#!/usr/bin/env python3
# ============================================================================
#  nodo_camara.py  -  Equipo NPC (Reto 2)
# ----------------------------------------------------------------------------
#  Detecta pilares ROJO / VERDE y el marcador MAGENTA en /camera/image_rect,
#  usando los rangos HSV calibrados en color_data.yaml.
#
#  Publica en /pilares (std_msgs/String) una lista legible de detecciones:
#  "R:320:45;G:120:30;M:500:80"
#  formato por pilar =  COLOR:x_centro:altura_px   separados por ';'
#  (vacio "" si no hay detecciones)
#       - COLOR  : R (rojo) / G (verde) / M (magenta)
#       - x_centro: columna del centro del bounding box (0=izq, ancho=der)
#       - altura : alto del bounding box en px  (mayor = mas cerca)
#
# ============================================================================

import os
import yaml
import cv2
import numpy as np

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge

# ---- VARIABLES AJUSTABLES DE DETECCION -------------------------------------
TOPIC_IN   = '/camera/image_rect'
TOPIC_OUT  = '/pilares'
YAML_PATH  = os.path.expanduser('~/wro_ws/tools/color_data.yaml')
MIN_ALTURA = 25      # alto minimo de blob en px para contar (filtra ruido)
MIN_AREA   = 80      # area minima de contorno en px (filtra motas)
DEBUG_VIEW = True    # True = abre ventana con detecciones dibujadas
# --------------------------------------------------------------------------

# nombre en YAML  ->  letra publicada  +  color BGR para dibujar el recuadro
# En YAML es donde quedan los codigos que configuramos de los colores
COLOR_MAP = {
    'red':     ('R', (0, 0, 255)),
    'green':   ('G', (0, 255, 0)),
    'magenta': ('M', (255, 0, 255)),
}


class NodoCamara(Node):
    def __init__(self):
        super().__init__('nodo_camara')
        self.bridge = CvBridge()
        self.frame = None

        self.rangos = self._cargar_yaml()   # {'red': (min,max), ...}

        qos = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=3,
        )
        self.create_subscription(Image, TOPIC_IN, self._cb_img, qos)
        self.pub = self.create_publisher(String, TOPIC_OUT, 10)

        if DEBUG_VIEW:
            cv2.namedWindow('nodo_camara', cv2.WINDOW_NORMAL)

        # procesa a ~20 Hz (la camara va a 30)
        self.create_timer(0.05, self._procesar)
        self.get_logger().info(
            f"nodo_camara v1 listo. Entrada={TOPIC_IN}  Salida={TOPIC_OUT}")

    # ---- cargar rangos HSV del YAML calibrado, que es donde quedan los codigos de los colores ----
    def _cargar_yaml(self):
        with open(YAML_PATH) as f:
            d = yaml.safe_load(f)
        rangos = {}
        for nombre in COLOR_MAP:
            c = d['colors'][nombre]
            rangos[nombre] = (list(c['min']), list(c['max']))
        self.get_logger().info(f"Rangos HSV cargados de {YAML_PATH}")
        return rangos

    # ---- callback imagen ----
    def _cb_img(self, msg: Image):
        try:
            self.frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"cv_bridge: {e}")

    # ---- mascara con wrap-around de Hue (rojo cruza 0) ----
    @staticmethod
    def _mascara(hsv, mn, mx):
        lo = np.array(mn)
        hi = np.array(mx)
        if mn[0] <= mx[0]:
            return cv2.inRange(hsv, lo, hi)
        m1 = cv2.inRange(hsv, np.array([0, mn[1], mn[2]]), hi)
        m2 = cv2.inRange(hsv, lo, np.array([179, mx[1], mx[2]]))
        return cv2.bitwise_or(m1, m2)

    # ---- bucle de proceso ----
    def _procesar(self):
        if self.frame is None:
            return
        frame = self.frame.copy()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        detecciones = []   # (letra, x_centro, altura, bbox) para publicar/dibujar

        for nombre, (mn, mx) in self.rangos.items():
            letra, bgr = COLOR_MAP[nombre]
            mask = self._mascara(hsv, mn, mx)
            # limpieza morfologica ligera: quita motas, rellena huecos
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                                    np.ones((3, 3), np.uint8))
            cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
            for c in cnts:
                if cv2.contourArea(c) < MIN_AREA:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                if h < MIN_ALTURA:
                    continue
                cx = x + w // 2
                detecciones.append((letra, cx, h, (x, y, w, h, bgr)))

        # --- publicar String legible ---
        partes = [f"{letra}:{cx}:{h}" for (letra, cx, h, _) in detecciones]
        self.pub.publish(String(data=';'.join(partes)))

        # --- ventana de debug ---
        if DEBUG_VIEW:
            for (letra, cx, h, (x, y, w, hh, bgr)) in detecciones:
                cv2.rectangle(frame, (x, y), (x + w, y + hh), bgr, 2)
                cv2.putText(frame, f"{letra} h{h}", (x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, bgr, 2)
            # linea central de referencia (separa izq/der)
            H, W = frame.shape[:2]
            cv2.line(frame, (W // 2, 0), (W // 2, H), (200, 200, 200), 1)
            cv2.putText(frame, f"{len(detecciones)} pilares", (10, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow('nodo_camara', frame)
            cv2.waitKey(1)


def main():
    rclpy.init()
    node = NodoCamara()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if DEBUG_VIEW:
            cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
