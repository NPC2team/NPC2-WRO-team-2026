#!/usr/bin/env python3
"""
Script simple de pruebas del robot NPC.
Conecta directamente al Pico Plus 2 por USB, sin necesidad de ROS 2.

ANTES DE USAR: parar el servicio para liberar el puerto USB
    sudo systemctl stop npc_bot.service

USO:
    python3 test_robot.py

AL TERMINAR: si quieres competir de nuevo, reactivar el servicio
    sudo systemctl start npc_bot.service
"""

import serial
import time
import sys

# --- Configuración ---
PUERTO = '/dev/ttyACM0'
BAUDIOS = 921600
VELOCIDAD_TEST = 0.3   # m/s para pruebas de motor (segura)
DURACION_TEST = 2.0    # segundos que dura cada movimiento

# --- Funciones auxiliares ---

def enviar(ser, comando):
    """Envía un comando al Pico con salto de línea al final."""
    ser.write((comando + '\n').encode())
    print(f'  → Enviado: {comando}')

def parar_todo(ser):
    """Para el motor y centra el servo."""
    enviar(ser, 'M,0.0')
    enviar(ser, 'S,0.0')

def leer_por_segundos(ser, segundos, filtro=None):
    """Lee y muestra mensajes del Pico por N segundos.
    Si filtro está dado ('IMU', 'ENC', 'POS'), solo muestra esos."""
    print(f'\n--- Leyendo mensajes por {segundos}s (Ctrl+C para cortar antes) ---')
    ser.reset_input_buffer()
    fin = time.time() + segundos
    try:
        while time.time() < fin:
            linea = ser.readline().decode(errors='ignore').strip()
            if linea:
                if filtro is None or linea.startswith(filtro):
                    print(f'  ← {linea}')
    except KeyboardInterrupt:
        print('\n  (cortado por Ctrl+C)')
    print('--- Fin ---\n')

def menu():
    print('\n' + '=' * 50)
    print('  PRUEBAS DEL ROBOT NPC (comunicación directa)')
    print('=' * 50)
    print('  SENSORES:')
    print('    1. Ver IMU     (yaw en tiempo real, 5s)')
    print('    2. Ver Encoder (ticks en tiempo real, 5s)')
    print('    3. Ver Odometría (POS, 5s)')
    print('')
    print('  MOTOR:')
    print(f'    4. Motor ADELANTE {DURACION_TEST}s ({VELOCIDAD_TEST} m/s)')
    print(f'    5. Motor ATRÁS    {DURACION_TEST}s (-{VELOCIDAD_TEST} m/s)')
    print('')
    print('  SERVO:')
    print(f'    6. Servo IZQUIERDA (-1.0) por {DURACION_TEST}s → centra')
    print('    7. Servo CENTRO (0.0)')
    print(f'    8. Servo DERECHA (+1.0) por {DURACION_TEST}s → centra')
    print('')
    print('  9. STOP total (motor 0, servo centro)')
    print('  0. Salir')
    print('=' * 50)
    return input('  Selecciona una opción: ').strip()

# --- Programa principal ---

def main():
    print(f'\nConectando al Pico en {PUERTO} a {BAUDIOS} baudios...')
    try:
        ser = serial.Serial(PUERTO, BAUDIOS, timeout=0.2)
    except serial.SerialException as e:
        print(f'\nERROR: no se pudo conectar al Pico.')
        print(f'  Detalle: {e}')
        print('')
        print('POSIBLES CAUSAS:')
        print('  1. El servicio npc_bot.service está corriendo y tiene el puerto ocupado.')
        print('     Solución:  sudo systemctl stop npc_bot.service')
        print('  2. El Pico no está enchufado o no aparece como /dev/ttyACM0.')
        print('     Verifica con:  ls /dev/tty*')
        sys.exit(1)

    time.sleep(0.5)  # esperar a que la conexión se estabilice
    ser.reset_input_buffer()
    print('Conectado.\n')

    try:
        while True:
            op = menu()

            if op == '1':
                leer_por_segundos(ser, 5, filtro='IMU')
            elif op == '2':
                leer_por_segundos(ser, 5, filtro='ENC')
            elif op == '3':
                leer_por_segundos(ser, 5, filtro='POS')
            elif op == '4':
                print(f'\n[MOTOR ADELANTE {VELOCIDAD_TEST} m/s por {DURACION_TEST}s]')
                enviar(ser, f'M,{VELOCIDAD_TEST}')
                time.sleep(DURACION_TEST)
                enviar(ser, 'M,0.0')
                print('Motor detenido.')
            elif op == '5':
                print(f'\n[MOTOR ATRÁS {VELOCIDAD_TEST} m/s por {DURACION_TEST}s]')
                enviar(ser, f'M,-{VELOCIDAD_TEST}')
                time.sleep(DURACION_TEST)
                enviar(ser, 'M,0.0')
                print('Motor detenido.')
            elif op == '6':
                print(f'\n[SERVO IZQUIERDA (-1.0) por {DURACION_TEST}s]')
                enviar(ser, 'S,-1.0')
                time.sleep(DURACION_TEST)
                enviar(ser, 'S,0.0')
                print('Servo centrado.')
            elif op == '7':
                print('\n[SERVO CENTRO]')
                enviar(ser, 'S,0.0')
            elif op == '8':
                print(f'\n[SERVO DERECHA (+1.0) por {DURACION_TEST}s]')
                enviar(ser, 'S,1.0')
                time.sleep(DURACION_TEST)
                enviar(ser, 'S,0.0')
                print('Servo centrado.')
            elif op == '9':
                print('\n[STOP TOTAL]')
                parar_todo(ser)
            elif op == '0':
                parar_todo(ser)
                print('\nSaliendo...')
                break
            else:
                print('  Opción no válida.')

    except KeyboardInterrupt:
        print('\n\nInterrupción por teclado. Parando todo por seguridad.')
        parar_todo(ser)

    finally:
        time.sleep(0.2)
        ser.close()
        print('Conexión cerrada.')

if __name__ == '__main__':
    main()
