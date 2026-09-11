/* ============================================================
 *  pico_firmware.ino
 *  ------------------------------------------------------------
 *  Firmware para la Pico Plus 2 (RP2350) de Proyecto Mahoraga
 *  Reto Abierto (Reto 1) — Equipo NPC
 *
 *  Que hace?:
 *    1. Leer encoder del motor por interrupciones
 *    2. Leer IMU BNO085 por I2C (Qwiic)
 *    3. Calcular odometría (x, y, theta, acc_yaw) a 100 Hz
 *    4. Recibir comandos seriales (M, S, STOP) por USB CDC
 *    5. Generar PWM para motor (VNH5019) y servo (Savox SC-1251MG)
 *    6. Publicar telemetría a 50 Hz por USB CDC
 *
 *  Protocolo serial (todos los mensajes terminan en '\n'):
 *    Pico → Pi5:
 *      POS,x,y,theta,acc_yaw    (posición + yaw acumulado sin wrap)
 *      IMU,yaw,qx,qy,qz         (yaw actual + cuaternión)
 *      ENC,ticks                (ticks crudos del encoder)
 *      BTN                      (botón físico presionado)
 *      OK                       (confirmación de comando)
 *      ERR,mensaje              (error o comando no reconocido)
 *    Pi5 → Pico:
 *      M,velocidad              (m/s, ej: M,0.80 o M,-0.20)
 *      S,steering               (-1.0 a +1.0, ej: S,-0.25)
 *      STOP                     (parada de emergencia)
 *
 *  Conexiones de hardware:
 *    Motor VNH5019:
 *      GPIO  8 → INB (dirección B)
 *      GPIO  9 → INA (dirección A)
 *      GPIO 10 → ENA (enable A, mantener HIGH)
 *      GPIO 12 → PWM (velocidad, 20 kHz)
 *      GPIO 13 → ENB (enable B, mantener HIGH)
 *    Servo Savox SC-1251MG:
 *      GPIO 15 → señal PWM (50 Hz, rango 15° a 165°, centro 90°)
 *    Encoder motor (48 CPR + reducción 34:1):
 *      GPIO  2 → Canal A (interrupción RISING)
 *      GPIO  3 → Canal B (lectura digital para sentido)
 *    Botón de arranque (pulsador a GND):
 *      GPIO 28 → señal del botón (INPUT_PULLUP, activo LOW)
 *    IMU BNO085 (Adafruit, Qwiic):
 *      GPIO  4 → SDA (I2C0)
 *      GPIO  5 → SCL (I2C0)
 *      Dirección I2C: autodetectada por la librería (0x4A o 0x4B)
 *    USB-C → Raspberry Pi 5 (Serial CDC, 921600 baud)
 * ============================================================ */

#include <Wire.h>
#include <Adafruit_BNO08x.h>

/* ============================================================
 *  CONSTANTES Y VARIABLES PARAMETRIZABLES
 * ============================================================ */

// --- Pines ---
constexpr uint8_t PIN_MOTOR_INA  = 9;
constexpr uint8_t PIN_MOTOR_INB  = 8;
constexpr uint8_t PIN_MOTOR_PWM  = 12;
constexpr uint8_t PIN_MOTOR_ENA  = 10;
constexpr uint8_t PIN_MOTOR_ENB  = 13;
constexpr uint8_t PIN_SERVO      = 15;
constexpr uint8_t PIN_ENCODER_A  = 2;
constexpr uint8_t PIN_ENCODER_B  = 3;
constexpr uint8_t PIN_BOTON      = 28;

// --- Comunicación ---
constexpr unsigned long SERIAL_BAUD = 921600;

// --- Motor (VNH5019) ---
constexpr int  PWM_FREQ_MOTOR    = 20000;   // 20 kHz, ultrasónico (sin ruido audible)
constexpr int  PWM_RESOLUTION    = 255;     // analogWrite estándar Arduino
// Valor calibrado empíricamente en pista:
//   Pedida 0.5 m/s con MS_TO_PWM=200 → tiempo en 2m: 5.05s y 4.80s
//   Velocidad real promedio: 0.406 m/s
//   Ajuste: 200 × (0.5 / 0.406) = 246
constexpr float MS_TO_PWM        = 246.0;   // ajustar si pruebas lo justifican
constexpr float MAX_VELOCITY_MS  = 1.20;    // máx velocidad permitida, aunque no hemos pasado de 0,7

// --- Servo (Savox SC-1251MG) ---
constexpr int SERVO_CENTER_DEG   = 90;      // centro físico
constexpr int SERVO_MIN_DEG      = 15;      // tope izquierdo permitido
constexpr int SERVO_MAX_DEG      = 165;     // tope derecho permitido
// El rango útil simétrico desde el centro es ±75° (90→15 y 90→165)
constexpr int SERVO_HALF_RANGE   = 75;

// --- Encoder ---
// Valor calibrado empíricamente:
//   Robot empujado 1.0 m → ENC delta promedio: 2007 ticks

constexpr float TICKS_POR_METRO  = 2007.0;

// --- Loops y frecuencias ---
constexpr unsigned long LOOP_ODOM_INTERVAL_US    = 10000;   // 100 Hz (cálculo odometría)
constexpr unsigned long LOOP_PUBLISH_INTERVAL_US = 20000;   // 50 Hz (envío telemetría)

// --- Botón ---
constexpr unsigned long BOTON_DEBOUNCE_MS = 50;             // tiempo mínimo entre detecciones

/* ============================================================
 *  VARIABLES GLOBALES
 * ============================================================ */

// --- IMU ---
Adafruit_BNO08x bno;
sh2_SensorValue_t sensorValue;
float yaw_rad   = 0.0;     // yaw actual normalizado a [-pi, +pi]
float qx = 0.0, qy = 0.0, qz = 0.0, qw = 1.0;  // cuaternión actual
bool  imu_ready = false;

// --- Encoder (volatile porque se modifican en ISR) ---
volatile long encoder_ticks = 0;
long          encoder_ticks_prev = 0;

// --- Odometría ---
float pos_x      = 0.0;    // posición x en metros (relativa al arranque)
float pos_y      = 0.0;    // posición y en metros
float pos_theta  = 0.0;    // orientación actual (igual a yaw_rad)
float acc_yaw    = 0.0;    // yaw acumulado SIN wrap (para contar giros desde Pi5)
float yaw_prev   = 0.0;    // yaw del loop anterior (para detectar wrap)
bool  yaw_initialized = false;

// --- Comandos recibidos ---
float cmd_velocity = 0.0;  // m/s (positivo adelante, negativo atrás)
float cmd_steering = 0.0;  // -1.0 (izquierda max) a +1.0 (derecha max)

// --- Botón ---
bool          boton_anterior = HIGH;       // último estado leído (HIGH = no presionado)
unsigned long t_ultima_deteccion_boton = 0; // timestamp ms del último BTN enviado

// --- Timers ---
unsigned long t_last_odom    = 0;
unsigned long t_last_publish = 0;

// --- Buffer para parsing serial ---
String serial_buffer = "";

/* ============================================================
 *  ISR DEL ENCODER (Interrupción de hardware)
 *  Se ejecuta cada vez que el canal A tiene flanco de subida.
 *  El signo se ajustó (++/--) para que ticks positivos
 *  correspondan a avance hacia adelante del robot.
 * ============================================================ */
void encoderISR() {
  if (digitalRead(PIN_ENCODER_B) == LOW) {
    encoder_ticks--;
  } else {
    encoder_ticks++;
  }
}

/* ============================================================
 *  SETUP
 * ============================================================ */
void setup() {
  // --- Serial USB ---
  Serial.begin(SERIAL_BAUD);
  // Esperamos opcionalmente al puerto serial (hasta 2 segundos)
  unsigned long t0 = millis();
  while (!Serial && (millis() - t0) < 2000) { delay(10); }
  Serial.println("BOOT,pico_firmware v1.0");

  // --- Pines del motor ---
  pinMode(PIN_MOTOR_INA, OUTPUT);
  pinMode(PIN_MOTOR_INB, OUTPUT);
  pinMode(PIN_MOTOR_ENA, OUTPUT);
  pinMode(PIN_MOTOR_ENB, OUTPUT);
  pinMode(PIN_MOTOR_PWM, OUTPUT);
  digitalWrite(PIN_MOTOR_ENA, HIGH);     // habilitar driver lado A
  digitalWrite(PIN_MOTOR_ENB, HIGH);     // habilitar driver lado B
  digitalWrite(PIN_MOTOR_INA, LOW);
  digitalWrite(PIN_MOTOR_INB, LOW);

  // Frecuencia PWM del motor (RP2350 en Arduino IDE de Earle Philhower)
  analogWriteFreq(PWM_FREQ_MOTOR);       // 20 kHz
  analogWriteResolution(8);              // 8 bits → 0-255
  analogWrite(PIN_MOTOR_PWM, 0);

  // --- Servo (usamos PWM manual a 50 Hz) ---
  // En Earle Philhower, podemos usar la librería Servo.
  // Para máxima portabilidad usamos la librería Servo estándar.
  setupServo();

  // --- Encoder con interrupciones ---
  pinMode(PIN_ENCODER_A, INPUT_PULLUP);
  pinMode(PIN_ENCODER_B, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(PIN_ENCODER_A), encoderISR, RISING);

  // --- Botón de arranque ---
  // INPUT_PULLUP: resistencia interna activada
  // El botón conecta a GND, por lo tanto presionado = LOW
  pinMode(PIN_BOTON, INPUT_PULLUP);
  boton_anterior = digitalRead(PIN_BOTON);

  // --- IMU BNO085 por I2C (Qwiic = I2C0 en GPIO 4/5) ---
  Wire.setSDA(4);
  Wire.setSCL(5);
  Wire.begin();
  if (bno.begin_I2C()) {
    imu_ready = true;
    // Activar reporte de Game Rotation Vector (cuaternión sin magnetómetro)
    // a 100 Hz (10 ms entre muestras)
    bno.enableReport(SH2_GAME_ROTATION_VECTOR, 10000);
    Serial.println("OK,IMU iniciado");
  } else {
    Serial.println("ERR,IMU no detectado en bus I2C");
  }

  // --- Inicializar timers ---
  t_last_odom    = micros();
  t_last_publish = micros();

  Serial.println("OK,setup completo");
}

/* ============================================================
 *  SETUP DEL SERVO
 *  Usamos la librería Servo estándar de Arduino, que en RP2350
 * ============================================================ */
#include <Servo.h>
Servo servo;

void setupServo() {
  servo.attach(PIN_SERVO, 1000, 2000);   // 1000-2000 us típico para servos hobby
  servo.write(SERVO_CENTER_DEG);          // centrar al inicio
}

/* ============================================================
 *  LOOP PRINCIPAL
 *  No usamos delay(). Tres tareas concurrentes:
 *    - Lectura IMU + odometría (100 Hz)
 *    - Publicación de telemetría (50 Hz)
 *    - Procesamiento de comandos seriales (continuo)
 * ============================================================ */
void loop() {
  unsigned long now = micros();

  // --- 1. Procesar comandos seriales (cada iteración) ---
  procesarSerial();

  // --- 2. Verificar botón físico (cada iteración) ---
  verificarBoton();

  // --- 3. Loop de odometría a 100 Hz ---
  if ((now - t_last_odom) >= LOOP_ODOM_INTERVAL_US) {
    t_last_odom = now;
    actualizarIMU();
    actualizarOdometria();
  }

  // --- 4. Publicación de telemetría a 50 Hz ---
  if ((now - t_last_publish) >= LOOP_PUBLISH_INTERVAL_US) {
    t_last_publish = now;
    publicarTelemetria();
  }
}

/* ============================================================
 *  ACTUALIZAR IMU
 *  Lee del BNO085 si hay nuevos datos disponibles. Extrae
 *  el cuaternión y calcula yaw en radianes.
 * ============================================================ */
void actualizarIMU() {
  if (!imu_ready) return;

  // Procesa eventos pendientes; puede no haber datos nuevos en cada llamada
  if (bno.getSensorEvent(&sensorValue)) {
    if (sensorValue.sensorId == SH2_GAME_ROTATION_VECTOR) {
      qx = sensorValue.un.gameRotationVector.i;
      qy = sensorValue.un.gameRotationVector.j;
      qz = sensorValue.un.gameRotationVector.k;
      qw = sensorValue.un.gameRotationVector.real;

      // Convertir cuaternión a yaw (rotación alrededor del eje Z)
      // Fórmula estándar: yaw = atan2(2(qw*qz + qx*qy), 1 - 2(qy² + qz²))
      float siny_cosp = 2.0 * (qw * qz + qx * qy);
      float cosy_cosp = 1.0 - 2.0 * (qy * qy + qz * qz);
      yaw_rad = atan2(siny_cosp, cosy_cosp);
    }
  }
}

/* ============================================================
 *  VERIFICAR BOTÓN
 *  Detecta bajada (HIGH→LOW) que indica presión.
 *  Aplica debounce simple: ignora nuevas presiones durante
 *  BOTON_DEBOUNCE_MS milisegundos.
 * ============================================================ */
void verificarBoton() {
  bool boton_actual = digitalRead(PIN_BOTON);
  unsigned long ahora_ms = millis();

  // Detectar bajada (HIGH → LOW = botón recién presionado)
  if (boton_anterior == HIGH && boton_actual == LOW) {
    // Verificar debounce temporal
    if ((ahora_ms - t_ultima_deteccion_boton) > BOTON_DEBOUNCE_MS) {
      Serial.println("BTN");
      t_ultima_deteccion_boton = ahora_ms;
    }
  }
  boton_anterior = boton_actual;
}

/* ============================================================
 *  ACTUALIZAR ODOMETRÍA
 *  Combina ticks del encoder con yaw del IMU para calcular
 *  posición global (x, y, theta).
 *  Mantiene acc_yaw sin wrap para contar giros desde Pi5.
 * ============================================================ */
void actualizarOdometria() {
  // 1. Leer ticks acumulados de forma atómica (volatile)
  noInterrupts();
  long ticks_now = encoder_ticks;
  interrupts();

  // 2. Calcular distancia recorrida desde la última lectura
  long delta_ticks = ticks_now - encoder_ticks_prev;
  encoder_ticks_prev = ticks_now;
  float delta_s = (float)delta_ticks / TICKS_POR_METRO;

  // 3. Actualizar posición usando el yaw ACTUAL como dirección de avance
  pos_x += delta_s * cos(yaw_rad);
  pos_y += delta_s * sin(yaw_rad);
  pos_theta = yaw_rad;

  // 4. Acumular yaw sin wrap (para contar giros en Pi5)
  if (!yaw_initialized) {
    yaw_prev = yaw_rad;
    yaw_initialized = true;
  } else {
    float delta_yaw = yaw_rad - yaw_prev;
    // Corregir el "salto" cuando cruza ±pi (wrap-around)
    if (delta_yaw >  PI) delta_yaw -= 2.0 * PI;
    if (delta_yaw < -PI) delta_yaw += 2.0 * PI;
    acc_yaw += delta_yaw;
    yaw_prev = yaw_rad;
  }
}

/* ============================================================
 *  PUBLICAR TELEMETRÍA
 *  Envía POS, IMU y ENC por Serial en formato CSV.
 * ============================================================ */
void publicarTelemetria() {
  // POS,x,y,theta,acc_yaw
  Serial.print("POS,");
  Serial.print(pos_x, 4);
  Serial.print(",");
  Serial.print(pos_y, 4);
  Serial.print(",");
  Serial.print(pos_theta, 4);
  Serial.print(",");
  Serial.println(acc_yaw, 4);

  // IMU,yaw,qx,qy,qz
  Serial.print("IMU,");
  Serial.print(yaw_rad, 4);
  Serial.print(",");
  Serial.print(qx, 4);
  Serial.print(",");
  Serial.print(qy, 4);
  Serial.print(",");
  Serial.println(qz, 4);

  // ENC,ticks
  Serial.print("ENC,");
  Serial.println(encoder_ticks);
}

/* ============================================================
 *  PROCESAR SERIAL
 *  Lee bytes disponibles, arma mensajes terminados en '\n'
 *  y los parsea.
 * ============================================================ */
void procesarSerial() {
  while (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '\n') {
      parsearComando(serial_buffer);
      serial_buffer = "";
    } else if (c != '\r') {
      serial_buffer += c;
      // Protección contra mensajes demasiado largos
      if (serial_buffer.length() > 64) {
        serial_buffer = "";
        Serial.println("ERR,buffer overflow");
      }
    }
  }
}

/* ============================================================
 *  PARSEAR COMANDO
 *  Reconoce: M,velocidad / S,steering / STOP
 * ============================================================ */
void parsearComando(String cmd) {
  cmd.trim();
  if (cmd.length() == 0) return;

  if (cmd.startsWith("M,")) {
    float v = cmd.substring(2).toFloat();
    // Limitar al rango permitido
    if (v >  MAX_VELOCITY_MS) v =  MAX_VELOCITY_MS;
    if (v < -MAX_VELOCITY_MS) v = -MAX_VELOCITY_MS;
    cmd_velocity = v;
    aplicarMotor(cmd_velocity);
    Serial.println("OK");
  }
  else if (cmd.startsWith("S,")) {
    float s = cmd.substring(2).toFloat();
    if (s >  1.0) s =  1.0;
    if (s < -1.0) s = -1.0;
    cmd_steering = s;
    aplicarServo(cmd_steering);
    Serial.println("OK");
  }
  else if (cmd == "STOP") {
    cmd_velocity = 0.0;
    cmd_steering = 0.0;
    aplicarMotor(0.0);
    aplicarServo(0.0);
    Serial.println("OK,STOP");
  }
  else {
    Serial.print("ERR,cmd desconocido:");
    Serial.println(cmd);
  }
}

/* ============================================================
 *  APLICAR MOTOR
 *  Convierte velocidad en m/s a PWM y configura dirección.
 *  VNH5019:
 *    INA=HIGH, INB=LOW  → atrás (en nuestro cableado)
 *    INA=LOW,  INB=HIGH → adelante (en nuestro cableado)
 *    INA=LOW,  INB=LOW  → freno (coast)
 * ============================================================ */
void aplicarMotor(float velocity_ms) {
  if (abs(velocity_ms) < 0.01) {
    // Velocidad ~0: detener motor
    digitalWrite(PIN_MOTOR_INA, LOW);
    digitalWrite(PIN_MOTOR_INB, LOW);
    analogWrite(PIN_MOTOR_PWM, 0);
    return;
  }

  // Determinar dirección (signos invertidos respecto al diagrama
  // estándar del VNH5019 para que velocidad positiva = adelante)
  if (velocity_ms > 0) {
    digitalWrite(PIN_MOTOR_INA, LOW);
    digitalWrite(PIN_MOTOR_INB, HIGH);
  } else {
    digitalWrite(PIN_MOTOR_INA, HIGH);
    digitalWrite(PIN_MOTOR_INB, LOW);
  }

  // Convertir magnitud a PWM
  int pwm_value = (int)(abs(velocity_ms) * MS_TO_PWM);
  if (pwm_value > PWM_RESOLUTION) pwm_value = PWM_RESOLUTION;
  analogWrite(PIN_MOTOR_PWM, pwm_value);
}

/* ============================================================
 *  APLICAR SERVO
 *  Convierte steering de [-1, +1] a ángulo del servo.
 *  Convención: +1 = giro derecha, -1 = izquierda
 *  Se aplica un signo negativo para invertir la convención
 *  del montaje físico actual del servo (queda al revés).
 * ============================================================ */
void aplicarServo(float steering) {
  int angle = SERVO_CENTER_DEG - (int)(steering * SERVO_HALF_RANGE);
  if (angle < SERVO_MIN_DEG) angle = SERVO_MIN_DEG;
  if (angle > SERVO_MAX_DEG) angle = SERVO_MAX_DEG;
  servo.write(angle);
}
