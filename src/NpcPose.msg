# ============================================================
# NpcPose.msg
# ------------------------------------------------------------
# Mensaje personalizado para la pose del robot NPC en WRO 2026.
# Combina posición 2D, orientación y yaw acumulado en un solo
# mensaje para mantener consistencia temporal.
#
# Publicado por: pico_bridge_node (en topic /npcpos)
# Consumido por: control_node, debug_node
#
# Campos:
#   x        : posición x del robot (metros, relativa al arranque)
#   y        : posición y del robot (metros, relativa al arranque)
#   theta    : orientación actual del robot (radianes, en [-pi, +pi])
#              Igual al yaw del IMU normalizado.
#   acc_yaw  : yaw acumulado SIN normalización (radianes).
#              Aumenta o disminuye continuamente con los giros.
#              Útil para contar giros de 90° (12 giros = 3 vueltas).
# ============================================================
float32 x
float32 y
float32 theta
float32 acc_yaw
