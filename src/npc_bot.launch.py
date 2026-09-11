#!/usr/bin/env python3
"""
Launch file del Reto Abierto

Arranca los 3 terminales en este orden:
1. Driver del LiDAR (LDROBOT STL-27L) -> publica /scan
2. Pico bridge (USB serial <-> ROS 2) -> publica /npcpos, /start
3. Control node (lazo de control 40 Hz) -> consume /scan y /npcpos

El control_node se inicia con un pequeño delay para que el LiDAR
y el bridge ya estén publicando antes de que entre en su estado BOOT.

IMPORTANTE: Esperar 40 segundos desde el encendido a que todo cargue y despues apretar el botón. 

Uso manual en practica:
    ros2 launch npc_bot npc_bot.launch.py

Uso automático en competencia:
    Lo arranca el servicio systemd "npc_bot.service" al boot.
"""

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # ----------------------------------------------------------
    # 1. LiDAR (LDROBOT STL-27L)
    # ----------------------------------------------------------
    lidar_pkg = get_package_share_directory('ldlidar_stl_ros2')
    lidar_launch_path = os.path.join(lidar_pkg, 'launch', 'stl27l.launch.py')

    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(lidar_launch_path)
    )

    # ----------------------------------------------------------
    # 2. Pico Bridge (USB serial <-> ROS 2)
    # ----------------------------------------------------------
    pico_bridge_node = Node(
        package='npc_bot',
        executable='pico_bridge',
        name='pico_bridge',
        output='screen',
        emulate_tty=True,
    )

    # ----------------------------------------------------------
    # 3. Control node (con delay de 2s para asegurar que /scan y
    #    /npcpos ya están publicándose)
    # ----------------------------------------------------------
    control_node = Node(
        package='npc_bot',
        executable='control_node',
        name='control_node',
        output='screen',
        emulate_tty=True,
    )

    control_node_delayed = TimerAction(
        period=2.0,
        actions=[
            LogInfo(msg='[npc_bot.launch] Arrancando control_node...'),
            control_node,
        ],
    )

    # ----------------------------------------------------------
    # Descripción completa
    # ----------------------------------------------------------
    return LaunchDescription([
        LogInfo(msg='[npc_bot.launch] Arrancando LiDAR...'),
        lidar_launch,
        LogInfo(msg='[npc_bot.launch] Arrancando pico_bridge...'),
        pico_bridge_node,
        control_node_delayed,
    ])
