#!/usr/bin/env python3
# ============================================================================
#  base_reto2.launch.py  -  Equipo NPC, WRO 2026 Future Engineers
# ----------------------------------------------------------------------------
#  Arranca los 5 nodos de BASE del Reto 2 (todo MENOS el control):
#     1. LiDAR            (ldlidar_stl_ros2 / stl27l.launch.py)
#     2. pico_bridge      (npc_bot)
#     3. camera_ros       (camera_node, RGB888 640x480)
#     4. camera_fixer     (camera_fixer_node)
#     5. nodo_camara      (script python en npc_bot)
#
#  El control_node_reto2 se lanza APARTE, en su propia terminal, para ver sus
#  logs limpios y poder reiniciarlo sin tumbar la base. Ver script aparte.
#
#  IMPORTANTE: este launch asume que los TRES workspaces ya estan sourceados
#  (camera_ws, lidar_ws, wro_ws). Por eso se lanza desde arrancar_base_reto2.sh,
#  que hace los source antes. No lanzar este archivo directo sin esos source.
#
#  Nodos como 'python3 script.py' se arrancan con ExecuteProcess; nodos de
#  paquete con Node o IncludeLaunchDescription.
# ============================================================================

import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # --- 1. LiDAR (incluye su propio launch file) ---
    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ldlidar_stl_ros2'),
                'launch', 'stl27l.launch.py')
        )
    )

    # --- 2. pico_bridge (nodo de paquete npc_bot) ---
    pico_bridge = Node(
        package='npc_bot',
        executable='pico_bridge',
        name='pico_bridge_node',
        output='screen',
    )

    # --- 3. camera_ros (nodo de paquete, con parametros) ---
    #     SIN name= : al lanzar a mano (ros2 run camera_ros camera_node) el nodo
    #     publica en /camera/image_raw, que es donde camera_fixer escucha.
    #     Poner name='camera_node' reubicaba los topics a /camera_node/image_raw
    #     y rompia la cadena (el fixer no recibia imagen). Por eso se omite.
    camera_ros = Node(
        package='camera_ros',
        executable='camera_node',
        output='screen',
        parameters=[{
            'format': 'RGB888',
            'width': 640,
            'height': 480,
        }],
    )

    # --- 4. camera_fixer (nodo de paquete) ---
    camera_fixer = Node(
        package='camera_fixer',
        executable='camera_fixer_node',
        name='camera_fixer',
        output='screen',
    )

    # --- 5. nodo_camara (script python suelto) ---
    #     DEBUG_VIEW se controla dentro del propio archivo. Para competencia
    #     conviene ponerlo en False para no abrir ventana ni gastar CPU.
    nodo_camara = ExecuteProcess(
        cmd=['python3',
             os.path.expanduser('~/wro_ws/src/npc_bot/npc_bot/nodo_camara.py')],
        output='screen',
    )

    # Arranque escalonado: LiDAR y camara primero, luego los que dependen
    # de que la imagen ya este publicandose (nodo_camara espera al fixer).
    return LaunchDescription([
        lidar_launch,
        pico_bridge,
        camera_ros,
        TimerAction(period=6.0, actions=[camera_fixer]),     # tras camera_ros (subido)
        TimerAction(period=12.0, actions=[nodo_camara]),     # tras camera_fixer (subido)
    ])
