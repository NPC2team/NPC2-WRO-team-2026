#!/usr/bin/env python3
# ============================================================================
#  Calibrador HSV autocontenido  -  Equipo NPC, WRO 2026 Future Engineers
# ----------------------------------------------------------------------------
#  Suscribe a /camera/image_rect (sensor_msgs/Image, bgr8/rgb8) y muestra:
#     - Ventana "Camara"  : imagen en vivo. CLICK izquierdo sobre un color
#                           para auto-centrar los sliders en ese pixel.
#     - Ventana "Mascara" : pixeles que caen dentro del rango HSV actual.
#     - Trackbars HSV (Hmin/Hmax/Smin/Smax/Vmin/Vmax).
#
#  Teclas:
#     r / g / m  -> selecciona color activo (red / green / magenta)
#     s          -> guarda TODOS los colores al YAML
#     q          -> salir
#
#  Compatibilidad: el YAML escrito tiene el MISMO formato que usa LazyBot
#  (colors -> nombre -> {min:[h,s,v], max:[h,s,v]}), e incluye soporte de
#  wrap-around de Hue para el rojo (cuando Hmin > Hmax).
#
#  Dependencias: solo rclpy, cv_bridge, opencv, numpy, pyyaml  (ya instaladas).
# ============================================================================

import os
import yaml
import cv2
import numpy as np

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# ---- AJUSTA AQUI SI HACE FALTA -------------------------------------------
TOPIC = '/camera/image_rect'          # topic corregido por camera_fixer
YAML_PATH = os.path.expanduser('~/npc_ws/color_data.yaml')  # donde guardar
COLORS = ['red', 'green', 'magenta']  # colores a calibrar
CLICK_MARGIN = 15                     # +/- al hacer click para centrar rango
# --------------------------------------------------------------------------

# Valores iniciales razonables por color (se sobreescriben al calibrar).
# Hue OpenCV: 0-179. Rojo cruza 0, asi que se calibra con wrap-around.
DEFAULTS = {
    'red':     {'min': [0, 120, 70],   'max': [10, 255, 255]},
    'green':   {'min': [40, 80, 60],   'max': [85, 255, 255]},
    'magenta': {'min': [140, 80, 70],  'max': [170, 255, 255]},
}

WIN_CAM = 'Camara'
WIN_MASK = 'Mascara'
WIN_CTRL = 'Controles HSV'
TRACK = ['Hmin', 'Hmax', 'Smin', 'Smax', 'Vmin', 'Vmax']


class CalibradorHSV(Node):
    def __init__(self):
        super().__init__('calibrador_hsv')
        self.bridge = CvBridge()
        self.frame = None
        self.active = COLORS[0]

        # Carga YAML existente si lo hay; si no, usa defaults.
        self.data = self._load_or_default()

        # Suscripcion best-effort (video en vivo, baja latencia).
        qos = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=3,
        )
        self.create_subscription(Image, TOPIC, self._cb, qos)

        # Ventanas + trackbars + callback de mouse.
        cv2.namedWindow(WIN_CAM, cv2.WINDOW_NORMAL)
        cv2.namedWindow(WIN_MASK, cv2.WINDOW_NORMAL)
        cv2.namedWindow(WIN_CTRL, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(WIN_CTRL, 400, 300)
        cv2.setMouseCallback(WIN_CAM, self._on_click)

        maxv = [179, 179, 255, 255, 255, 255]
        for name, mx in zip(TRACK, maxv):
            cv2.createTrackbar(name, WIN_CTRL, 0, mx, lambda x: None)

        self._sliders_from_color(self.active)
        self.get_logger().info(
            f"Calibrador listo. Color activo: {self.active}. "
            f"Teclas: r/g/m=color  s=guardar  q=salir")

    # ---- ROS callback ----
    def _cb(self, msg: Image):
        try:
            # camera_fixer entrega bgr8; si fuese rgb8 cv_bridge lo maneja igual
            # y lo pedimos como bgr8 para que OpenCV muestre colores correctos.
            self.frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"cv_bridge: {e}")

    # ---- mouse: click para auto-centrar ----
    def _on_click(self, event, x, y, flags, param):
        if event != cv2.EVENT_LBUTTONUP or self.frame is None:
            return
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        if y >= hsv.shape[0] or x >= hsv.shape[1]:
            return
        h, s, v = [int(c) for c in hsv[y, x, :]]
        self.get_logger().info(f"Click {self.active}: H={h} S={s} V={v}")
        m = CLICK_MARGIN
        self._set_sliders([max(0, h - m), max(0, s - m), max(0, v - m)],
                          [min(179, h + m), min(255, s + m), min(255, v + m)])

    # ---- helpers de sliders ----
    def _set_sliders(self, mn, mx):
        vals = [mn[0], mx[0], mn[1], mx[1], mn[2], mx[2]]
        for name, val in zip(TRACK, vals):
            cv2.setTrackbarPos(name, WIN_CTRL, int(val))

    def _read_sliders(self):
        g = lambda n: cv2.getTrackbarPos(n, WIN_CTRL)
        mn = [g('Hmin'), g('Smin'), g('Vmin')]
        mx = [g('Hmax'), g('Smax'), g('Vmax')]
        return mn, mx

    def _sliders_from_color(self, color):
        c = self.data['colors'][color]
        self._set_sliders(c['min'], c['max'])

    # ---- mascara con wrap-around de Hue (igual que LazyBot) ----
    @staticmethod
    def _make_mask(hsv, mn, mx):
        lo = np.array(mn)
        hi = np.array(mx)
        if mn[0] <= mx[0]:
            return cv2.inRange(hsv, lo, hi)
        # wrap-around (rojo): dos rangos [0..Hmax] + [Hmin..179]
        m1 = cv2.inRange(hsv, np.array([0, mn[1], mn[2]]), hi)
        m2 = cv2.inRange(hsv, lo, np.array([179, mx[1], mx[2]]))
        return cv2.bitwise_or(m1, m2)

    # ---- YAML ----
    def _load_or_default(self):
        if os.path.exists(YAML_PATH):
            try:
                with open(YAML_PATH) as f:
                    d = yaml.safe_load(f)
                if d and 'colors' in d:
                    for c in COLORS:
                        d['colors'].setdefault(c, dict(DEFAULTS[c]))
                    self.get_logger().info(f"YAML cargado de {YAML_PATH}")
                    return d
            except Exception as e:
                self.get_logger().warn(f"YAML ilegible ({e}), uso defaults")
        return {'color_space': 'HSV',
                'colors': {c: dict(DEFAULTS[c]) for c in COLORS}}

    def _save(self):
        # vuelca los sliders actuales al color activo antes de guardar
        mn, mx = self._read_sliders()
        self.data['colors'][self.active] = {'min': mn, 'max': mx}
        os.makedirs(os.path.dirname(YAML_PATH), exist_ok=True)
        with open(YAML_PATH, 'w') as f:
            yaml.safe_dump(self.data, f, default_flow_style=None, sort_keys=False)
        self.get_logger().info(f"GUARDADO -> {YAML_PATH}")

    # ---- bucle de dibujo (se llama desde main) ----
    def render(self):
        if self.frame is None:
            return
        mn, mx = self._read_sliders()
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        mask = self._make_mask(hsv, mn, mx)
        masked = cv2.bitwise_and(self.frame, self.frame, mask=mask)

        disp = self.frame.copy()
        cv2.putText(disp, f"Activo: {self.active}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(disp, "r/g/m=color  s=guardar  q=salir", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow(WIN_CAM, disp)
        cv2.imshow(WIN_MASK, masked)

    def switch(self, color):
        # guarda los sliders del color saliente en memoria y carga el nuevo
        mn, mx = self._read_sliders()
        self.data['colors'][self.active] = {'min': mn, 'max': mx}
        self.active = color
        self._sliders_from_color(color)
        self.get_logger().info(f"Color activo: {color}")


def main():
    rclpy.init()
    node = CalibradorHSV()
    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.01)
            node.render()
            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                break
            elif k == ord('r'):
                node.switch('red')
            elif k == ord('g'):
                node.switch('green')
            elif k == ord('m'):
                node.switch('magenta')
            elif k == ord('s'):
                node._save()
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
