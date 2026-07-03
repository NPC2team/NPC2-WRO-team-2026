
## **NPC – WRO FUTUROS INGENIEROS 2026** 

## **CONTENIDO** 

## **1. Introducción e Información del Equipo**
- a. Introducción 
- b. Miembros del Equipo 
## **2. Vehículo** 
- a. Descripción del Vehículo 
- b. Fotos del Vehículo 
## **3. Videos de Pruebas del Vehículo** 
- a. Reto 1 – Open Challenge 
- b. Reto 2 – Obstacle Challenge 
## **4. Movilidad y Diseño Mecánico (Criterio 1)** 
- a. Chasis 
- b. Sistema de Tracción 
- c. Sistema de Dirección 
## **5. Arquitectura de Potencia y Sensores (Criterio 2)** 
- a. Sistema de Potencia 
- b. Power Budget 
- c. Sensores 
- d. Diagrama de Comunicación 
- e. Ubicación de Sensores 
- f. Diagrama de Cableado 
- g. Decisión de Diseño
## **6. Arquitectura de Software y Estrategia de Obstáculos  (Criterio 3)** 
- a. Visión General
- b  Estructura del Código
- c. Tópicos 
- d. Firmware del Pico 2 
- e. Estrategia del Reto Abierto
- f. Diagrama de Flujo de Reto Abierto
- g. Métricas de Desempeño del Reto Abierto 
- h. Nodos y Tópicos de Reto con Obstáculos
- i. Estrategia del Reto con Obstáculos
- j. Detección de Pilares R/G/M (cámara)
- k. Diagrama de Flujo de Reto con Obstáculo
- l. Métricas de Desempeño del Reto con Obstáculos
- m. Ajustes Realizados en Ambos Retos
## **7. Pensamiento Sistémico y Decisiones de Ingeniería (Criterio 4)** 

## **8. Instrucciones de Reproducibilidad (Criterio 5)** 



## **1. Encabezado e Información del Equipo** 

## 1a. Introducción 
<div>
<img width="316" height="411" align="left" alt="Equipo" src="https://github.com/user-attachments/assets/75947953-eac8-472f-b4b6-771bddc59407" /><br>
   
Somos el equipo **NPC (Non Playable Character)**, este es nuestro segundo año en competencias de la WRO, con el objetivo de lograr un vehículo verdaderamente autónomo que supere con éxito los retos de la competencia WRO    Futuros Ingenieros 2026 a Nivel Nacional y nos permita obtener nuestro cupo en la Final Internacional de Puerto Rico. 

Vu Tue Anh, compitió el año pasado en la categoría de Misiones Roboticas, mientras que Leonardo y Juan participaron en la categoría de Futuros Ingenieros, llegando a la Final Nacional de Venezuela donde obtuvimos el 5to Lugar, mientras que en un invitacional en Weifang, China logramos el 1er Lugar. 
</div>
<br clear="left" />

## 1b. Miembros del Equipo 

## **Juan Ignacio Gonzalez** 

<img width="300" height="210" align="left" alt="foto de juan" src="https://github.com/user-attachments/assets/ed233a77-1e34-493c-bbb3-09d09d80df08" /><br>
Hola soy Juan, soy venezolano/español y tengo 16 años, actualmente estudio 4to año de bachillerato y miembro del Club de Robótica del Colegio Jefferson.  Este es mi segundo año en la competencia de la WRO de Futuros Ingenieros. En 2025, junto con Leonardo obtuvimos el 5to Lugar en la Final Nacional y el 1er Lugar en un invitacional en Weifang, China. 

Mis aportes al equipo se han enfocado en el código de Arduino IDE/Python, así como la realización de pruebas de los distintos componentes y de los retos. 

<br clear="left" />

## **Leonardo Carrasquero** 

<img width="210" height="300" align="left" alt="Foto Leo" src="https://github.com/user-attachments/assets/3321f65f-eee9-4a1c-8590-d9dd36cd5ec3" /><br>
Hola soy Leo, venezolano/italiano de 16 años, estudio 4to año de bachillerato y soy miembro del Club de Robótica del Colegio Jefferson 2024.  Al igual que Juan, este es mi segundo año en la categoría de Futuros Ingenieros y este año quiero lograr participar en la Final Internacional de Puerto Rico. 

Mis contribuciones se enfocaron en la investigación de componentes, diseño e impresión de piezas 3D, ensamblaje del robot, así como programación en Python y ROS2. 

<br clear="left" />

## **Vu Tue Anh** 

<img width="210" height="300" align="left" alt="Foto Vu" src="https://github.com/user-attachments/assets/1f55c34e-20b2-4f6b-848f-cb1276342bbd" /><br>
Hola soy Vu, de origen vietnamita y llevó 3 años viviendo en Venezuela y soy compañera de 4to año de Juan y Leonardo, en el Colegio Jefferson. Este también es mi segundo año en competencias de la WRO, pero el año pasado estuve en la categoría de misiones roboticas. Este año quise cambiar y tener el reto de participar en Futuros Ingenieros. 

Para nuestro proyecto, fui responsable en la realización de pruebas, así como de la documentación y registro fotográfico. 

<br clear="left" />

## **Alfredo Gonzalez**

<img width="210" height="300" align="left" alt="PHOTO-2026-06-04-21-09-27" src="https://github.com/user-attachments/assets/48676392-0ae0-44b2-8602-3c6cad144d51" /><br>
Alfredo, es nuestro coach y de profesion matemático. 

Él también es nuestro profesor de robótica en el Colegio Jefferson y ha estado desde 2023 paticipando en ompetencias de la WRO en Venezuela, dirigiendo a varios equipos del colegio en las distintas categorias, con participaciones en las Regionales, Final en Venezuela, Final Internacional y diversos invitacionales.

<br clear="left" />

## **Foto del Equipo Junto y Foto en China** 


<img width="1000" height="500" alt="Foto Equipo China" src="https://github.com/user-attachments/assets/0fcc130a-4b6b-41c9-a679-5f67b65756d1" />

<img width="1000" height="500" alt="3DC51F0D-4A7F-49F5-A332-7C0CE98BB8BD" src="https://github.com/user-attachments/assets/334253b8-bd11-4a9b-96b2-d55186c25b6b" />


## **2.Robot** 

## 2a. Descripción del Robot 

**“Proyecto Mahoraga”** es nuestro vehículo para Futuros Ingenieros 2026, representa una evolución significativa con respecto a **“Crazy Diamond” (WRO 2025)**, con quien ya logramos triunfos y a quien le agradecemos el aprendizaje. Proyecto Mahoraga presenta mejoras en hardware, diseño y software que nos permitirá ejecutar con éxito los retos de Futuros Ingenieros 2026. Abordaremos con detalle en este Readme y en el Engineering Journal las características del Robot, el proceso de diseño, construcción y programación, así como las decisiones y obstáculos que tuvimos en el camino, con la finalidad de que sea posible replicar por cualquier entusiasta de la robótica como nosotros. 

## 2b. Fotos del Robot 

<table>
  <tr>
    <td align="center">
      <b>Vista Frontal</b><br>
      <img src="https://github.com/user-attachments/assets/b4a8942e-1439-43c1-a7ca-33edc2647366"<img width="400" height="320"> 
    </td>
    <td align="center">
      <b>Vista Trasera</b><br>
      <img src="https://github.com/user-attachments/assets/90ec6a1e-9b9b-4096-9ffc-a29e07064918" width="400" height="320">
    </td>
    <td align="center">
      <b>Lado Izquierdo</b><br>
      <img src="https://github.com/user-attachments/assets/66ecf1d0-42eb-4086-8b54-f46e6d13c84b" width="400" height="320">
    </td>
  </tr>
  <tr>
    <td align="center">
      <b>Lado Derecho</b><br>
      <img src="https://github.com/user-attachments/assets/6423f7da-b81e-492e-8be2-071ec206ab03" width="400" height="320">
    </td>
  <td align="center">
  <b>Vista de Arriba</b><br>
  <img src="https://github.com/user-attachments/assets/095f60eb-c609-4bc3-b138-825c379ec7ad" width="400" height="320">
</td>
    <td align="center">
      <b>Vista de Abajo</b><br>
      <img src="https://github.com/user-attachments/assets/eb93e29e-50c1-4a9a-acb2-6969fd807bcf" width="400" height="320">
    </td>
  </tr>
</table>

## **3. Videos de Pruebas del Vehículo** 

3a. Reto 1 – Open Challenge 

**Link YouTube** 
(https://youtube.com/shorts/lqm2GCjuBmU?feature=share)

3b. Reto 2 – Obstacle Challenge 

**Link YouTube** 

## **4. Movilidad y Diseño Mecánico (Criterio 1)** 

En este apartado documentamos la ficha técnica de la configuración mecánica final de **Proyecto  Mahoraga**.  En  el  Engineering  Journal  (Sección  4)  incluimos  la  descripción completa  del proceso  de  diseño,  las  mejoras sobre  nuestro  robot 2025,  los ajustes realizados sobre la versión inicial de Proyecto Mahoraga y los cálculos detallados del Ackerman, torque y velocidad. 

## 4a. Chasis 

Compuesto por 2 niveles, con un subnivel adicional y un compartimiento hecho a la medida para la batería Lipo S3 11.1V. Esto con la finalidad de hacer más eficiente el uso del espacio y lograr obtener un robot más pequeño y ágil. Las piezas fueron impresas en 3D, dándonos mayor flexibilidad en el diseño y permitiéndonos adecuar los espacios a los componentes mecánicos y eléctricos de Proyecto Mahoraga. 

<img width="604" height="426" alt="Chasis Comentado" src="https://github.com/user-attachments/assets/6b80a166-bae0-440d-9ea4-06bb7c6f8add" />


|**Atributo**|**Descripción**|
|---|---|
|Tipo|Personalizado, diseñado en Fusion|
|Material|PLA impreso en 3D(Bambu Lab P2S)|
|Dimensiones|234 × 135 × 126 mm|
|Distribución vertical|2 pisos modulares + 2 subniveles|
|Distancia entre ejes(batalla)|142 mm|
|Distancia entrepivotes|97 mm|
|Peso(sin cámara)|1.100g (límite reglamentario: 1500g)|


Todos los archivos en STL/3MF están en **/models** (chasis de abajo y de arriba, soportes de motor y servo, carcasa y engranajes del diferencial y motor, espaciadores, repisa, canales de cables con tapas). 

**_En el Engineering Journal en la sección 4.1 comentamos la evolución del chasis luego de un proceso iterativo, así como su comparativo con la versión que manejamos en 2025._** 

## 4b. Sistema de Tracción 

<img width="310" height="371" align="left" hspace="6" alt="Traccion4" src="https://github.com/user-attachments/assets/a12c207c-572d-4ec8-92f4-fbbe8cc1bc22" />

- Elegimos un motor Pololu 34:1 Metal Gearmotor 25Dx67L mm MP 12V con Encoder 48 CPR por su alta calidad y más que velocidad buscábamos precisión y torque, por lo que al incluir el diferencial nos generó 2.006 ticks por metro medidos por el encoder, permitiéndonos un control más fino, tanto para la medición de las distancias recorridas como para las maniobras del estacionamiento. 

 - Reutilizamos el diferencial utilizado por Crazy Diamond en 2025, ajustándolo al menor ancho de Proyecto Mahoraga e imprimimos un nuevo engranaje para el motor porque el eje era de menor diámetro y necesitaba otro flange para ajustar correctamente. 

 - El motor es manejado por un Pololu VNH5019 de alta estabilidad, con buen manejo de energía que lo protege de cambios bruscos de dirección y le permite mantener la precisión al robot. 

 - Incorporamos unas ruedas de 11mm de ancho de aluminio con neumático de goma, menos anchas que el estándar de 25mm, lo cual nos permite reducir el ancho, disminuir la fricción y mejora la estabilidad efectiva pese, al menor ancho su mayor peso permite bajar el centro de gravedad del motor.

<br clear="left" />

|**Atributo**|**Descripción / Valor**|
|---|---|
|Tipo|Tracción trasera (RWD)|
|Motor|Pololu 34:1 Metal Gearmotor 25Dx67L mm MP 12V|
|Velocidad Lineal|1,1231 m/s|
|Encoder|48 CPR en el eje del motor|
|Torque|1,65 Kg/cm(Sin Diferencial) 2,32 Kg/cm(Con Diferencial)|
|Resolución calibrada|2.006 ticks/metro(medido enpruebas)|
|Driver del Motor|Pololu VNH5019 Tecnología MOSFET|
|Diferencial|Impreso 3D propio (Gear Diferencial + Gear Box)|
|Eje trasero|KYX Racing acero (Tamiya DT04)|
|Ruedas|64 mm aluminio, ancho 11 mm + neumático de goma|

**_En el Engineering Journal en la sección 4.2 comentamos porque elegimos estos componentes y la comparativa con otras opciones, adicionalmente detallamos el cálculo de ticks por metro del encoder, la velocidad lineal y el torque del motor._**

## 4c. Sistema de Dirección 

<img width="331" height="352" align="left" hspace="6" alt="Direccion" src="https://github.com/user-attachments/assets/3a22cd53-615c-4a26-9979-4e6cee0f2961" />

Uno de los principales retos de este año era que el vehículo debía ser más ágil, para lo cual había que reducir su tamaño y mejorar su capacidad de giro. Con batalla 142 mm y pivotes 97 mm, el robot recorre 34,2 cm para girar 90°, frente a los 48,2 cm del chasis 2025 (−29%). 

Los C Hub o portamanguetas de dirección fueron integrados en el chasis de abajo, permitiendo el mayor cruze que podía aportar el servo. El servo Savox SC-1251MG aporta precisión de ángulo de giro al ser digital, tener engranajes metálicos y ser coreless, permitiéndole además una alta velocidad de respuesta 0.09s/60°. 

A diferencia del 2025, colocamos el servo detrás de las ruedas delanteras. Esta decisión liberó el espacio frontal para colocar el LiDAR en posición baja y adelantada. 

<br clear="left" />
<br>

|**Atributo**|**Descripción / Valor**|
|---|---|
|Geometría|Ackermann|
|Servo|Savox SC-1251MG (digital, coreless,<br>engranajes metálicos)|
|Par servo|9.0 kg·cm@6.0 V|
|Velocidad servo|0.07 s/60°|
|Posición del servo|Detrás de las ruedas delanteras|
|Servo saver|Tamiya TT-02 Hi-Torque|
|Manguetas|KYX Racingaluminio(Tamiya DT04)|
|Tie rods|M3 ajustables(uxcell)|
|Ángulo degiro máximo|50°|
|Batalla(L)|142 mm|
|Pivotes(W)|97 mm|
|Radio degiro(R)|217,7 mm a 40°|
|Distancia para 90°|341,90 mm|


**_En el Engineering Journal en la sección 4.3 describimos más ampliamente los componentes de la dirección, las ventajas del principio Ackerman, así como los cálculos para obtener el radio de giro y la distancia necesaria para completar un giro de 90 grados. Comparamos estos resultados con los que obtuvimos en el 2025 y explicamos las mejoras._** 


## **5. Arquitectura de Potencia y Sensores (Criterio 2)** 

En este apartado documentamos la ficha técnica del sistema de alimentación, distribución de potencia y arquitectura de sensores para **Proyecto Mahoraga**. 

**_En el Engineering Journal (sección 5) se encuentran las justificaciones de selección de los componentes batería/reguladores, diagramas de cableado completos y presupuesto de energía (power Budget), así como justificación de selección de sensores y su proceso de calibración._** 

## 5a. Sistema de Potencia 

|**Componente**|**Modelo**|**Especificaciones**|
|---|---|---|
|Batería|Zeee LiPo 3S|11.1 V nominal, 3.000 mAh, 50C, conector T|
|Regulador Principal<br>(lógica)|Pololu D24V90F5|5V salida, 9 A continuos|
|Regulador  Servo|Pololu D36V50F5|5V salida, 5.5 A continuos|
|Motor Driver|Pololu VNH5019|Rango Operativo 5,5 a 24V, Cpacidad 12 A|

La bateria 3S nos permite alimentar correctamente el motor Pololu 34:1 25Dx67L MP 12V y sacar provecho de su potencia. 

**Decisión clave:** Distribución dual de reguladores 5V. El D24V90F5 (9A) alimenta toda la lógica del robot (Raspberry Pi 5, Pico Plus 2, LiDAR, IMU, TOF, lógica del VNH5019). El D36V50F5 (5.5A) alimenta exclusivamente el servo Savox SC-1251MG, que tiene picos de corriente durante giros bruscos o choques. Esto aísla los transitorios del servo del riel de lógica sensible, evitando reinicios del Raspberry Pi 5 o del Pico Plus 2. 

<img width="845" height="634" alt="Distribucion de Potencia" src="https://github.com/user-attachments/assets/cbb05f86-15c2-4bf1-b885-bf6c1c0fd992" />


## 5b. Power Budget 

Como se observa en la tabla del Power Budget, el uso de los 2 reguladores nos da holgura y mitiga el riesgo en picos de voltaje. 

**Capacidad regulador lógica (9 A) y servo (5.5 A), ambos con margen de seguridad ≥50% respecto al consumo pico estimado.**

|**Componente**|**Voltaje**|**Corriente**<br>**típica**|**Corriente**<br>**pico**|**Notas**|
|---|---|---|---|---|
|Raspberry Pi 5 (16GB) +<br>NVMe|5 V|1.5 A|3.0 A|Fuente oficial recomienda 5A|
|Active Cooler RPi 5|5 V|0.05 A|0.1 A|Ventilador PWM|
|SSD M.2 NVMe Silicon<br>Power|3.3 V|0.3 A|0.5 A|Alimentado vía NVMe Base|
|Pico Plus 2 (RP2350)|5 V|0.05 A|0.15 A|Alimentado desde RPi vía USB|
|Terminal PiCowbell|5 V|<0.01 A|<0.01 A|Solo terminales / reset|
|LiDAR STL-27L|5 V|0.3 A|0.3 A|21.600 mediciones/s, 10Hz|
|IMU BNO085|3.3 V (Qwiic)|0.015 A|0.025 A|Bajo consumo|
|VL53L4CD ToF ×2|3.3 V (Qwiic)|0.020 A c/u|0.05 A c/u|Sensor láser pulsado|
|Cámara Global Shutter|3.3 V (FPC)|0.25 A|0.4 A|Alimentada por RPi|
|SparkFun Qwiic<br>MultiPort|3.3 V|<0.001 A|<0.001 A|Pasivo|
|Servo Savox<br>SC-1251MG|5 V|0.5 A|3.5 A (stall)|Posibilidad de picos en giros y<br>choques|
|Motor Pololu 34:1 12V|11.1 V (LiPo)|0.5 A|5.0 A (stall)|Alimentación directa|
|Encoder magnético|3.3 V|0.01 A|0.015 A|Alimentado por Pico 2|
|VNH5019 (lógica)|5 V|<0.01 A|<0.01 A|Solo lógica; potencia va por LiPo|
|**TOTAL bus lógica (5V**<br>**vía D24V90F5)**<br>**TOTAL bus servo (5V**<br>**via D36V50F5)**<br>**Bus 11.1V MOTOR**<br>**(directo)**||**~2.2 A**<br>**~0.5 A**<br>**~0.5 A**|**~4.0 A**<br>**~3.5 A**<br>**~5.0 A**|Margen: +125 % pico, +309%<br>continuo<br>Margen: +57 % pico, +1.000%<br>continuo<br>Margen: +140 % pico|
|**TOTAL desde LiPo 3S**||**~3.2 A**|**~9.0 A pico**||


## 5c. Sensores 

Uno de los upgrades más importantes que hicimos en **Proyecto Mahoraga** fue tener sensores de alto nivel. El LiDAR era una adición necesaria para el manejo de los obstáculos de una manera robusta. La ubicación y control preciso de los movimientos del robot queda cubierta con el IMU BNO085 y el Encoder. La cámara es un upgrade más profesional vs la Pixy que utilizamos en 2025 y los TOF VL53L4CD son un nivel más sofisticado que los ultrasónicos HC-SR04. 

|**Sensor**|**Modelo**|**Función**|
|---|---|---|
|<img width="110" height="110" alt="LiDAR STL-27L" src="https://github.com/user-attachments/assets/3231313c-9930-4cb0-8cdd-8c09de7f08a4" /> |LiDAR 360° <br> LDROBOT STL-27L|Con 21.600 mediciones por segundo a 10 Hz (10<br>vueltas de 2.160 mediciones) es muy útil para la<br>detección de paredes y obstáculos.|
|<img width="110" height="110" alt="IMU" src="https://github.com/user-attachments/assets/64021dd6-e882-4b43-94db-420a91359841" />|IMU 9-DOF <br> Adafruit BNO085|Entrega orientación absoluta directamente como<br>quaternion, permitiendo una fácil orientación<br>absoluta.|
|<img width="110" height="100" alt="TOF" src="https://github.com/user-attachments/assets/5ed9f11f-feae-4101-a55e-bd5bdbb29eb4" />|ToF láser <br> Adafruit<br>VL53L4CD|Prácticamente sin punto ciego, distancia lateral<br>izq/der (1–1300 mm) a 100 Hz, es muy útil para<br>tareas de precisión como estacionar.|
|<img width="100" height="110" alt="CamaraGS" src="https://github.com/user-attachments/assets/28cd9c8b-eb2c-449b-baf1-88d52ed59e4e" /> |Cámara Raspberry Pi <br> Global Shutter<br>|Visión por computador para detectar pilares<br>rojos/verdes. Al ser Global Shutter limita las<br>distorsión de objetos en movimiento.|
|<img width="100" height="90" alt="GS Lens" src="https://github.com/user-attachments/assets/82a42c9a-cfe0-4fa4-acbb-b78bad9f0970" />|Lente CCTV M12 <br>2.8mm F2.0|Campo de visión amplio para captura 96°>|
|<img width="110" height="110" alt="Encoder" src="https://github.com/user-attachments/assets/c9b0380f-ce44-4107-9fe8-7cd2a6e6303e" />|Magnetic Encoder<br>Pololu|48 CPR motor, 2.006 ticks/m calibrados|

**_En el Engineering Journal, sección 5.3 abordamos con detalle porque elegimos estos componentes._** 

## 5d. Topología de Comunicaciones 

Se caracteriza por una topología híbrida en estrella de alto rendimiento, donde la Raspberry Pi 5 actúa como el nodo central de procesamiento, conectada punto a punto mediante interfaces dedicadas a la cámara Global Shutter (vía MIPI CSI-2), al LiDAR STL27L (vía un puente USB-UART) y a una co-procesadora Raspberry Pico Plus 2 (vía USB-CDC). A su vez, la Pico Plus 2 funciona como un nodo secundario de control en tiempo real, gestionando un bus I2C/Qwicc compartido en paralelo para los sensores críticos de navegación (2 sensores de distancia TOF VL53L4CD y la IMU BNO085) y utilizando líneas independientes GPIO/PWM para el control directo de actuadores y hardware de movimiento, que incluyen un encoder, el driver de motor VNH5019 y un servo Savox SC-1251MG. 

<img width="558" height="347" alt="Topologia de Comunicación2" src="https://github.com/user-attachments/assets/b38bd3fd-9669-4113-bf3e-4ea2c285b41a" />


## 5e. Ubicación de Sensores 

- **LiDAR:** primer piso, adelantado, altura óptima (FOV a 4,5 cms del piso) para detectar paredes y obstáculos de la pista (10 cm). 

- **Cámara:** segundo piso, inclinada 60 grados hacia abajo, captura el plano del suelo y los pilares con buena anticipación. 

- **IMU:** segundo piso, lo más alejado posible del motor y driver para minimizar EMI, pese a estar conectado por Qwiic, se fijó en una protoboard para garantizar no tuviera vibraciones. 

- **ToF #1 (izq) y ToF #2 (der):** apuntando perpendicular a las ruedas, retraídos 15 mm de la superficie exterior para eliminar la zona muerta del sensor. 

<img width="942" height="600" alt="Ubicación de Sensores" src="https://github.com/user-attachments/assets/1314b2d3-25ad-4afa-8bad-3a2b8fac8868" />

<br>

## 5f. Diagrama de Cableado 

<img width="2800" height="2000" alt="esquematico" src="https://github.com/user-attachments/assets/feb72cbb-3bc7-460f-871f-41e487800fb9" />

**_Diagrama completo de conexiones eléctricas: ver schemes/conexiones-del-robot.pdf._** 

**_Detalle de cada conexión (pin a pin) en el Engineering Journal sección 5.5 ._** 

## **6. Arquitectura de Software y Estrategia de Obstáculos (Criterio 3)** 

## 6a. Visión General 

El software del robot **Proyecto Mahoraga** está construido sobre ROS 2 Jazzy corriendo en Ubuntu 24.04 en una Raspberry Pi 5 (16 GB), con un microcontrolador Pimoroni Pico Plus 2 (RP2350) encargándose de la lectura de sensores de bajo nivel y el control de actuadores. La arquitectura sigue un patrón distribuido de dos capas: 

• Raspberry Pi 5 (capa de alto nivel): ejecuta nodos ROS 2 para percepción, toma de decisiones y control a 40 Hz. 

• Pico Plus 2 (capa de bajo nivel): ejecuta un firmware basado en Arduino a mayor frecuencia para lectura del IMU, conteo del encoder, integración de odometría, generación de PWM del motor y del servo. 

La comunicación entre las dos capas ocurre por USB serial (921600 baudios) usando un protocolo CSV liviano, conectado a topicos ROS 2 mediante un nodo puente dedicado. 

<img width="612" height="474" alt="Nodos y Topicos Reto 1" src="https://github.com/user-attachments/assets/350644a9-b4a9-480d-b60c-c625360d443f" />

## 6b.Estructura del Código

```
src/
├── firmware/
│   └── pico_firmware.ino          # Firmware C++ del Pico (Arduino)
├── npc_bot/                       # Paquete ROS 2 Python
│   ├── pico_bridge_node.py        # Puente USB ↔ topics ROS 2
│   ├── control_node.py            # Reto 1: Open Challenge
│   ├── control_node_reto2.py      # Reto 2: Obstacle Challenge
│   ├── nodo_camara.py             # Visión (solo Reto 2)
│   └── calibrador_hsv.py          # Calibración HSV interactiva
├── npc_interfaces/
│   └── msg/NpcPose.msg            # Mensaje custom {x,y,θ,acc_yaw}
├── launch/
│   ├── npc_bot.launch.py          # Lanza Reto 1 completo
│   └── base_reto2.launch.py       # Lanza Reto 2 completo
└── systemd/
    └── npc_bot.service            # Arranque Automatico 
```


## 6c.Tópicos 

Se desarrolló un esquema de comunicación basado en tópicos, estableciendo los nodos suscriptores y publicador fundamental para la comunicación en ROS2.

|**Topic**|**Tipo**|**Publicador**|**Suscriptor**|**Descripción**|
|---|---|---|---|---|
|/scan|sensor_msgs/LaserScan|Driver LiDAR|control_node|Scan LiDAR 360° @10 Hz|
|/npcpos|npc_interfaces/NpcPose|pico_bridge|control_node|Pose del robot (x, y, theta,<br>acc_yaw) @50 Hz|
|/start|std_msgs/Empty|pico_bridge|control_node|Señal de inicio (botón)|
|/cmd_motor|std_msgs/Float32|control_node|pico_bridge|Velocidad del motor en m/s|
|/cmd_servo|std_msgs/Float32|control_node|pico_bridge|Dirección en [-1.0, +1.0]|
|/imu|sensor_msgs/Imu|pico_bridge|(debug)|Datos del IMU filtrados|
|/encoder|std_msgs/Int32|pico_bridge|(debug)|Ticks crudos del encoder|


## 6d. Firmware del Pico 2 

El Pico Plus 2 ejecuta un firmware basado en Arduino (un único archivo.ino) que maneja todas las operaciones de tiempo real de las que la RPi5 no debe encargarse. 

**Responsabilidades** 

- Lectura del IMU a 100 Hz vía Qwiic I2C (Adafruit BNO085, con fusión sensorial 9-DOF onboard) 
- Conteo del encoder vía interrupción por hardware en GPIO 2 (Canal A) y lectura digital en GPIO 3 (Canal B), cuadratura de un solo flanco 
- Integración de odometría a 100 Hz (calcula Δx, Δy, Δtheta y los acumula) 
- Generación de PWM del motor a 20 kHz (sobre el rango audible) vía driver Pololu VNH5019 
- Generación de PWM del servo a 50 Hz para el servo de dirección Savox SC-1251MG 
- Lectura del botón de arranque en GPIO 28 (INPUT_PULLUP, activo LOW) 
- Publicación de telemetría a la Pi5 a 50 Hz vía USB serial 

**Protocolo Serial de Comunicación RPi5 y Pico2** 

**Pico → Pi5** (50 Hz cada uno): 

POS <x, y, theta, acc_yaw> **`→`** Odometría 
IMU <yaw, qx, qy, qz> **`→`** Quaternión del IMU 
ENC < ticks > **`→`** Conteo del encoder 
BTN **`→`** Botón presionado (evento) 
BOOT,...  OK,...  ERR,... **`→`** Mensajes de estado 

**Pi5 → Pico** (a demanda): 

M < velocidad_ms > **`→`** Velocidad del motor en m/s 
S < direccion > **`→`** Servo, rango [-1.0, +1.0] 
STOP **`→`** Parada de emergencia 

## 6e. Estrategia del Reto Abierto 

La lógica del Reto Abierto está organizada en 4 pilares funcionales, cada uno abordando una preocupación distinta. Esta descomposición hizo más clara la discusión de diseño y modular la implementación. 

**Pilar 1. Localización y Conteo de Giros** 

Objetivo: saber dónde está el robot y cuántas esquinas ha girado (meta: 12 giros = 3 vueltas completas). 

**Enfoque** : 

- Odometría calculada en el Pico usando los ticks del encoder y el yaw del IMU 

- `theta` publicado normalizado a [-π, +π] 

- `acc_yaw` publicado (valor acumulado del yaw del IMU) 

- Conteo de giros realizado al detectar el cruce (esquina) y no depender del cálculo acumulado del IMU que puede verse afectado por el efecto drifting. 

**Pilar 2. Detección de Esquinas y Sentido de Recorrido** 

El robot debe detectar cuándo ha llegado a una esquina, decidir hacia qué lado girar, y en qué sentido (CW o CCW) seguirá toda la carrera. Esta metodología era igual a la que empleamos en 2025, pero en aquel momento lo hicimos con ultrasónicos y ahora contamos con un LiDAR, esto nos permitió hacer la detección de una forma más robusta. 

Al encontrarnos a 0,7 metros de la pared central el LiDAR revisa los laterales en busca de aperturas (lecturas mayores a 1m). Sin embargo, no dependimos de una medida única frontal del LiDAR y 2 laterales, le pedimos la mediana de ±5° de la medición frontal y 2° de mediciones laterales en vez de solo una medición a +90° y -90°. En el caso de nuestro LiDAR que nos da 2.160 mediciones en cada vuelta, esto representa 6 mediciones por cada grado, permitiéndonos tener 60 mediciones frontales (10x6) y 12 en cada lateral (2x6), dando más robustez y evitar falsas señales. 

|**Condición**|**Umbral**|**Propósito**|
|---|---|---|
|Distancia frontal cerca|mediana(FRONTAL ±5°) < 0.7 m|Hay una pared al frente|
|Debounce espacial|dist desde último giro > 1.0 m|Evitar contar dos veces<br>la misma esquina|
|Apertura lateral confirmada|mediana(LATERAL 2° en lado<br>del giro) > 1.0 m|Es una esquina real, no<br>una medición errónea|

<table>
  <tr>
    <td align="center">
      <b>Detección Frontal</b><br>
     <img width="400" height="320" alt="Frontal70cms" src="https://github.com/user-attachments/assets/f0689cbe-4bd5-44dd-9f91-780d9d763d0a" />
    </td>
    <td align="center">
      <b>Detección Lateral de Esquina</b><br>
      <img width="400" height="320" alt="Lateral100cms" src="https://github.com/user-attachments/assets/d2e309f0-7445-41b5-a012-50918cacea9b" />
    </td>
  </tr>
</table>

```
if self.sentido_giro is None:
    apertura_izq = mediana(LATERAL_IZQ)
    apertura_der = mediana(LATERAL_DER)
    if apertura_izq > 1.0 and apertura_der < 1.0:
        self.sentido_giro = 'CCW'
    elif apertura_der > 1.0 and apertura_izq < 1.0:
        self.sentido_giro = 'CW'
    elif ambos_abiertos:
        self.sentido_giro = 'CCW' if apertura_izq >= apertura_der else 'CW'
    else:
        return  # esperar al siguiente loop, no decidir aún
```

Una vez que en la primera esquina se determina el sentido de los giros, en las siguientes esquinas el LiDAR, solo busca aperturas hacia esa dirección. 



**Pilar 3. Control de Navegación y Centrado de Pared** 

Establecimos 2 esquemas de control de navegación: El Heading y el Centrado de Paredes donde el que tenga la corrección más importante tiene preferencia. Asi tenemos que: 

Heading: Una vez que el LiDAR detecta un desvío importante o detecto un cruce y se actualiza el nuevo ángulo destino +/-90° según sea la dirección, se produce un error alto que activa el heading y hace girar el servo. La agresividad del giro está controlada por un P-controller con dos ganancias diferenciadas. Una ganancia más agresiva (KP_Giro) cuando el error es superior a 15° y una ganancia menor (KP_Rect) cuando el error se reduce a 15°, esto hace que una vez que el error (desviación con el objetivo se reduce) el angulo de giro se suaviza evitando un sobrecruce o oscilaciones buscando el objetivo. 

```
error = norm_ang(self.pose.theta - self.section_angle)

if self.turning:
    str_angle = error * KP_GIRO    # 1.91
else:
    str_angle = error * KP_RECT    # 0.48

str_angle = clamp(str_angle, -1.0, 1.0)
```


Centrado de Paredes: Tal como va haciendo las mediciones para detectar las aperturas, también va realizando mediciones para calcular desviaciones respecto al centro de la pista 

<img width="400" height="320" align="right" alt="Centrado de Paredes" src="https://github.com/user-attachments/assets/6350c33e-c6ee-4556-ac09-e184c207aea2" />

```
dist_der = mediana(WALL_DER)   # +75° a +77° en el frame del robot
dist_izq = mediana(WALL_IZQ)   # -77° a -75° en el frame del robot
```

El algoritmo de centrado no actúa todo el tiempo; solo se activa si se cumplen estas tres condiciones simultáneamente:

```
if (dist_der + dist_izq < 1.1
    and dist_desde_giro > 0.4
    and not self.turning):
```

Esto garantiza que no haya la medición de error cuando hay una apertura, que no se active el centrado cuando está girando o apenas lleva 40cms desde el último giro e interfiera en el giro. 
```
pos = dist_der - dist_izq
    str_lateral = clamp(pos * KP_LATERAL, -0.5, +0.5)
```
<br clear="right" />

Si las condiciones se cumplen, el código calcula cuánto debe corregir la dirección. 

Cálculo del error (pos): Resta la distancia derecha menos la izquierda. 

- Si el robot está perfectamente centrado, dist_der y dist_izq serán iguales, por lo que pos = 0 (no se necesita corrección). 

- Si el robot se arrima a la izquierda, dist_izq se reduce, haciendo que pos sea un valor positivo (orden de corregir hacia la derecha). 

Control Proporcional (Kp): Multiplica ese error por una constante de ganancia (KP_LATERAL). A mayor desviación, mayor será la fuerza del giro corrector, tal como hacíamos en el Heading con 2 Kp. 

Saturación (clamp): Limita el comando de dirección (str_lateral) entre -0.5 y +0.5 para evitar que un cálculo extremo haga que el robot derrape o pierda el control. 

El robot ya viene calculando el Heading (str_heading) apuntando hacia el angulo objetivo. El código compara las magnitudes absolutas del Heading y del Centrado (str_lateral). Si la necesidad de corregir la posición lateral (str_lateral) para no chocar con la pared es más drástica que la de mantener la orientación actual (str_heading), el control de centrado toma prioridad absoluta y devuelve str_lateral. De lo contrario, el robot ignora el centrado fino y sigue su rumbo normal. 

```
if abs(str_lateral) > abs(str_heading):
        return str_lateral    # regla: gana la corrección más fuerte
return str_heading
```

**Velocidad Adaptativa:** Estipulamos 2 velocidades distintas para las curvas y para las rectas, permitiendo la mayor estabilidad. Las velocidades establecidas en 0.25 m/s y 0.4 m/s son el 50% de las velocidades iniciales que establecimos y que están por debajo de la velocidad teórica que habíamos calculado. Sin embargo, está velocidades en la práctica nos permitió tener mayor nivel de confiabilidad y evitar choques por retraso en alguna detección. 

```
if self.turning:
    velocidad = VELOCIDAD_CURVA      # 0.25 m/s
else:
    velocidad = remap(abs(str_angle),
                      in_min=0.0, in_max=1.0,
                      out_min=VELOCIDAD_RECTA,   # 0.4 m/s
                      out_max=VELOCIDAD_CURVA)   # 0.25 m/s
```

**Pilar 4. Fin de Carrera** 

Después de completarse el 12° giro (turn_count == 12), el estado transita a FINISH_APPROACH, donde: 

- Heading y Centrado de Pared permanecen activos (el robot debe quedarse en el corredor mientras frena) 

- La detección de esquinas se desactiva 

- La velocidad se escalona en tres zonas según la distancia frontal con el objetivo de frenar cuando se encuentre a 1,5 m de la pared frontal (el centro del tramo recto que es de 3,0 metros). Si por alguna razón se pasará de 1,2 m, está abierta la posibilidad de retroceder. 

|**Distancia frontal**|**Velocidad**|**Comportamiento**|
|---|---|---|
|> 2.0 m|VELOCIDAD_RECTA × 0.7 = 0.28 m/s|Aproximación lenta|
|1.5 — 2.0 m|VELOCIDAD_CURVA = 0.25 m/s|Frenado|
|1.2 — 1.5 m|0|Banda de parada objetivo|
|< 1.2 m|-0.2 m/s|Marcha atrás|


**Máquina de Estados** 

La máquina de estados de alto nivel tiene cinco estados: 

<img width="860" height="190" alt="Maquina de Estados Reto1" src="https://github.com/user-attachments/assets/50964103-af37-4f0c-9a91-b8d0e3deeeef" />


|**Estado**|**Comportamiento**|
|---|---|
|**BOOT**|Espera el primer scan del LiDAR y el primer mensaje de pose. No<br>inicializa nada más.|
|**READY**|Motor y servo en 0. Espera /start (botón). Al presionar el botón, captura<br>section_angle = theta actual como rumbo de carrera.|
|**RUNNING**|Control completo: detección de esquinas, heading, centrado de pared,<br>velocidad, conteo de giros.|
|**FINISH_APPROACH**|Heading y centrado activos, sin detección de esquinas, perfil de<br>velocidad basado en la distancia frontal.|
|**STOPPED**|Motor y servo en 0. Estado terminal.|

## 6f. Diagrama de Flujo de Reto Abierto

<img width="1911" height="1077" alt="Reto1" src="https://github.com/user-attachments/assets/8688b286-6c20-4c30-901a-c8fbc9baaf0d" />


## 6g. Métricas de Desempeño del Reto Abierto 

Después de 3 días de pruebas físicas en la pista oficial WRO: 

|**Métrica**|**Resultado**|
|---|---|
|Detección de sentido (CW o CCW)|100% correcta con el enfoque de detección<br>en la primera esquina y luego de ajustes.|
|Precisión del conteo de giros|12/12 giros contados correctamente, no se<br>generan dobles giros por restricciones<br>colocadas para ello, aprendidas en WRO<br>2025|
|Tasa de completación de vueltas|Luego de ajustes, Estable con múltiples<br>corridas exitosas de 3 vueltas, 1 solo choque<br>por fallo en lectura de apertura, corregido|
|Precisión de posición de parada|Consistentemente dentro de la banda 1,2 a 1,5m|
|Posición lateral durante rectas|< 5 cm de desviación del centro del<br>corredor, mucho más robusto con el control<br>dual Heading y Centrado|
|Heading después de completar un giro|Dentro de 5° del objetivo|
|Tiempos Promedios en Pruebas| 40 segundos|

Luego de correcciones menores logramos obtener tiempos de 40 segundos para dar las 3 vueltas, mas eficientes a los que obtuvimos en la Regional 1 de Miranda, que si bien logramos realizar el reto, el robot tardó en arrancar por un problema con el engrane del motor que quedó flojo al consumirse por el calor y la fricción generado por el uso. 

**Solución:** Reimprimir el engranaje en resina de Nylon, mucho mas resistente al calor y a la fricción que el PLA que utilizamos en el engranaje anterior. Una vez solucionados en las prácticas volvimos ha obtener tiempos entre 42 y 38 segundos. 

<img width="722" height="400" alt="Resultados Regional 1 2026" src="https://github.com/user-attachments/assets/dfc9c8f8-c718-4969-aeb3-4f4e9d9558e1" />

## 6h. Nodos y Tópicos de Reto con Obstáculos 

Adicional a los nodos y tópicos del Reto Abierto (Seccion 6a y 6b del Readme), en el Reto con Obstáculos interviene la cámara y por eso se incluye un nodo_camara y tiene su propio codigo de control denominado "control_node_reto2". En cuanto a topicos ademas de los del Reto Abierto se incluye el tópico de detección de los pilares "/pilares"

<img width="612" height="480" alt="Nodos y Topicos Reto 2" src="https://github.com/user-attachments/assets/3785e9bd-e193-4e83-b3f7-aa99fce97854" /><br>

### Topicos ROS 2 principales

| Topico | Tipo | Publicador → Suscriptor |
|---|---|---|
| /scan | sensor_msgs/LaserScan | lidar → control |
| /npcpos | npc_interfaces/NpcPose | pico_bridge → control |
| /start | std_msgs/Empty | pico_bridge → control (botón físico) |
| /cmd_motor | std_msgs/Float32 (m/s) | control → pico_bridge |
| /cmd_servo | std_msgs/Float32 (−1…+1) | control → pico_bridge |
| /pilares | std_msgs/String (`R:cx:h;G:cx:h;M:cx:h`) | nodo_camara → control_reto2 |

## 6i. Estrategia del Reto con Obstáculos 

La lógica del Reto con Obstáculos está organizada en una navegación distinta a la del Reto Abierdo, donde la detección de esquinas era fundamental para hacer los cruces. En este reto abandonamos eso y si bien mantenemos los Estados simples, la navegación se hace siguiendo 3 capas de orientación que conviven 1) Ruta Proyectada 2) Recorte por Color y 3) SpiderSense.

| Capa | Función | Sensor primario |
|---|---|---|
| **C1 — Ruta Proyectada** | Ray marching: abanico ±60° de candidatos, vecinos ±25°, paso `castR=0.075 m` | LiDAR |
| **C2 — Recorte por color** | Si pilar rojo → solo candidatos derechos; si verde → solo izquierdos | Cámara |
| **C3 — SpiderSense** | Reflejo lateral: si distancia <22 cm en 25°–75°, atenúa el lado correspondiente ÷3 | LiDAR |

**Capa 1 — Ruta Proyectada (Ray Marching)**

<img width="460" height="480" align="left" alt="Ruta Proyectada" src="https://github.com/user-attachments/assets/7153eb87-3d9f-4852-8b41-2012b0090877" />

En la La Capa 1, el LiDAR reporta un abanico de direcciones candidatas frente al robot (de −60° a +60° en intervalos de 2° - 60 lecturas) y cada una se convierte en una "Ruta Viable", entonces para cada una se calcula un "score" para determinar cual es la trayectoria ideal o best_dir. Ese score combina 2 cosas, 1) Cuán lejos puede ir el robot en esa dirección sin chocar con algo y 2) Que tan desviada está esa dirección respecto al rumbo objetivo de la pista. La dirección ganadora es la propuesta inicial de hacia dónde dirigirse.

**Función de score (Capa 1):**
```
score = min(d, DIST_SAT) / DIST_SAT − PESO_RUMBO × |desvío_del_rumbo|
DIST_SAT = 1.6 m       PESO_RUMBO = 0.0015
```

Adicionalmente para cada uno de las 60 rutas candidatas, se aplica el principio de "ray marching" donde no solo se observa el punto candidato si no que también se mide un radio de 7,5 cm de cada lado para cerciorarnos que el robot pueda caber por esa ruta, si en la ruta candidata se choca con algun objeto al ver el ray marching, entonces esa ruta es descartada o su distancia maxima se limita hasta donde si cabe el ray marching.  

<br clear="left" />

**Capa 2 — Recorte por Color**

<img width="460" height="440" align="left" alt="Capa2" src="https://github.com/user-attachments/assets/5c05023b-fa03-45a2-8d99-c9e73ed0e801" />

La cámara aporta dos datos por cada pilar visible: qué color es y en qué posición horizontal de la imagen está (el centro del blob detectado, en píxeles).
El nodo nodo_camara.py convierte cada frame de BGR a HSV, aplica máscaras de color con los rangos HSV calibrados y publica el centroide y la altura del blob más grande de cada color en el topic /pilares. <br>
<br>
La altura en píxeles funciona como proxy de distancia: un pilar cercano se ve grande, uno lejano se ve pequeño. Cuando hay un pilar relevante, la Capa 2 hace una conversión sencilla: traduce la posición en píxeles a un ángulo en el frame del robot usando el FoV de 88° de la lente CCTV 2,8 mm, y luego fuerza el best_dir a un lado u otro del pilar, con un margen seguro de unos 15°. Si el pilar es rojo, el robot se desvía hacia la derecha del pilar, estableciendo una zona prohibida a su izquierda, donde ninguna ruta es factible; mientras que si el pilar es verde, las ruta viables estan hacia la izquierda y las prohibidas a la derecha. 

<br clear="left" />
<br>

**Capa 3 — SpiderSense**

La Capa 3 "SpiderSense" es el reflejo de emergencia para casos donde las paredes laterales o los obstaculos estan muy cerca, para esto el LiDAR dos sectores laterales (25° a 75° en cada lado del robot) y calcula la distancia mínima en cada uno. Si la distancia del lado izquierdo cae por debajo de 22 cm y el robot está virando hacia la izquierda (steering < 0), entonces el comando de steering se divide entre 3. Lo mismo para el lado derecho. La doble condición (peligro lateral + giro hacia el peligro) es clave, si el robot está virando hacia el lado contrario, no hay riesgo de colisión inminente. Al dividir entre 3 el steering lo que se busca es atenuar el angulo de giro para evitar la colisión lateral 

```
Si d_izq < 22 cm AND robot vira a la izquierda -> steering / 3
Si d_der < 22 cm AND robot vira a la derecha -> steering / 3  
```

**Fin de carrera:** 

Como no tenemos giros y esquinas como en el Reto Abierto, que para finalizar la carrera, contabamos 12 giros, entonces establecimos una medición acumulada de giro en terminos absoluto del IMU |acc_yaw| y que cuando este supere los 900°, equivalenten a 2,5 vueltas, entonces buscar el proximo color magenta, que justamente es el estacionamiento y cuando lo vea se detenga en esa sección, siguiendo la estrategia del Reto Abierto, es decir, parar cuando este entre 1,3m y 1,5m de la pared frontal de esa sección.


`|acc_yaw| > 900°` **AND** detección de blob
magenta con altura ≥ 60 px (caja de parada), luego parada por
distancia frontal como en Reto 1.

## 6j. Detección de Pilares R/G/M (cámara)

<img width="300" height="320" align="left" alt="Detección de Pilares" src="https://github.com/user-attachments/assets/68cab891-b796-4743-8e43-a9954c33ba31" />

nodo_camara.py convierte el frame BGR a HSV, aplica máscaras de color y publica el centroide y altura del mayor blob de cada color detectado.

**Rangos HSV calibrados en pista oficial (lente CCTV 2.8 mm):**

| Color | H min | H max | S min | S max | V min | V max |
|---|---|---|---|---|---|---|
| **Rojo** (pilar) | 5 | 14 | 80 | 255 | 80 | 255 |
| **Verde** (pilar) | 47 | 96 | 50 | 255 | 60 | 255 |
| **Magenta** (caja de parada) | 158 | 179 | 70 | 255 | 70 | 255 |

**Nota crítica del rojo:** H_min = 5` está deliberadamente arriba de 0 para evitar las líneas naranjas del piso de la pista WRO, confusión que sucedieron en las primeras prácticas. 

<br clear="left" />
<br>

## 6k. Diagrama de Flujo de Reto con Obstáculos

<img width="600" height="1075" alt="Reto2" src="https://github.com/user-attachments/assets/8b36ad02-b3b0-473f-b923-e1e8d9394cd6" />


## 6l. Métricas de Desempeño del Reto con Obstáculos 

Después de 5 días de pruebas físicas en la pista oficial WRO: 

|**Métrica**|**Resultado**|
|---|---|
|Detección de Ruta Ideal)|100% correcta cuando se practica sin obstaculos (12 rondas de 3 vueltas c/u). Con obstaculos (200 obstaculos con promedio de 5 por vuelta de 40 vueltas). <br> En el 10% de los casos la evasión ha causado un desvio incorrecto (21/200)|
|Tasa de Detección de Obstáculos|96% de obstaculos detectados correctamente (192/200 obstaculos). <br>  Dificultad de detección cuando vehículo se desvia mucho y cámara no detecta por el FoV| 
|Tasa de Evasión de Obstáculos|80% de obstaculos detectados correctamente (160/200 obstaculos). <br> 4% por no detección, 10% por falta de espacio para evadir y 6% por chocar el obstáculo|. 
|Tasa de completación de vueltas|40% de Éxito de vuelta completa con evasión (16 de 40 vueltas). Ha mejorado desde que redujimos velocidad.|
|Precisión de posición de parada|0% Se está deteniendo un giro antes por detección erronea del magenta. Identificado el problema pero dando prioridad a otros ajustes|
|Tiempos Promedios en Pruebas| 32 segundos por Vuelta|

Data de prueba recopilada hasta el 29/6, que ha ido mejorando con ajustes de velocidad. 

## 6m. Ajustes Realizados en Ambos Retos

- Inicialmente diseñamos una detección de sentido pre-arranque más ambiciosa analizando discontinuidades del LiDAR mientras el robot estaba estacionario. La idea era detectar el lado en donde estaban las discontinuidades más importantes, para detectar hacia qué lado estaba la apertura, pero la tasa de éxito dependía mucho de la posición inicial del robot por lo que pasamos a una estrategia más reactiva como la comentada en el _Pilar 2 - Sección 6e. Estrategia del Reto Abierto_. 

- Al comienzo habíamos establecido, que una vez que el robot comenzara a girar, saliera del modo giro cuando el error con respecto al ángulo objetivo ya se hubiera reducido a 45° (la mitad), esto para evitar sobregiros por la velocidad pasando el P Controller de un KP_GIRO más alto a  KP_RECT mas gradual, pero obtuvimos muchos subgiros y activación de aperturas no reales que provocaban nuevos giros. La solución: 

   - Luego de un proceso iterativo redujimos el error para pasar de KP_GIRO a KP_RECT de 45° a 15° 
   - Redujimos las velocidades a la mitad, quedando en 0.4 m/s en rectas y 0.25 m/s en curvas. Favoreciendo confiabilidad vs velocidad. 

Con estos ajustes logramos una tasa de éxito muy elevada en el Reto Abierto, incluso con cambios en el tamaño del cuadro central a 1,4m y 1,8m por lado. La velocidad reducida y el esquema dual del P-Controller han permitido que los ajustes post giro se han muy leves y a veces imperceptibles. 

- **Proyecto Mahoraga** en el Reto con Obstáculos arrancaba todo el tiempo recto y no cruzaba pese a detectar rutas en las aperturas, razón por lo que tuvimos que recalibrar el mecanismo de score que daba a cada ruta candidata, disminuyendo la penalización de no ir a la dirección actual. Pese a recalibrar, logramos el efecto contrario donde siempre se inclinaba con mas fuerza a donde hubiera la mayor apertura, provocando giros mas agresivos hacia la ruta ideal, está pendiente evaluar si limitar el giro maximo que podía hacer en cada iteracción para suavizar el comportamiento.

- Para el Reto con Obstáculos también vimos la necesidad de reducir la velocidad y así dar mas tiempo para la detección de obstáculos y la maniobra de evasión, quedando en 0.3 m/s en rectas y 0.20 m/s en curvas.

Con estos ajustes hemos logrado una mejora en la tasa de éxito en el Reto con Obstáculos, quedando pendiente aún mas pruebas y el ajuse de velocidad, capacidad de giro y posiblemente esttructurar una maniobra de retroceso cuando no sea posible hacer la evasión del obstáculo. Adicionalmente está pendiente la estrategía del estacionamiento.

## 7. Pensamiento Sistémico y Decisiones de Ingeniería (Criterio 4)

Esta sección documenta cómo los subsistemas del robot trabajan juntos, las restricciones que dieron forma al diseño, las decisiones principales con sus alternativas, y el historial de iteraciones. El análisis técnico extendido (con cálculos, código y diagnósticos está en el **Engineering Journal, sección 7**.

## 7a. Diagrama de Bloques del Sistema

<img width="1100" height="600" alt="Diagrama de Subsistemas" src="https://github.com/user-attachments/assets/6603342d-d4cd-45a9-a2ca-d9efe30c329e" />

## 7b. Interacción entre Subsistemas

| Subsistema A | Subsistema B | Interacción |
|---|---|---|
| LiDAR STL-27L | Control (RPi 5) | Publica /scan a 10 Hz → control extrae sectores frontal/laterales |
| Cámara GS + lente 2.8 mm | Nodo de visión (RPi 5) | Detecta pilares R/G/M y publica /pilares (formato R:cx:h;G:cx:h) |
| Pico Plus 2 | RPi 5 | UART USB 921600 baud, CSV → topics /npcpos, /imu, /encoder, /start |
| IMU BNO085 | Pico Plus 2 | I²C 100 Hz → integración con encoder produce POS,x,y,θ,acc_yaw |
| Encoder motor | Pico Plus 2 | Interrupción RISING en GP2 + lectura GP3 → odometría a 100 Hz |
| Control (RPi 5) | Pico Plus 2 | Publica /cmd_motor (m/s) y /cmd_servo (-1..+1) a 40 Hz |
| Pico Plus 2 | VNH5019 | INA/INB + PWM 20 kHz (GP8/9/12) → tracción |
| Pico Plus 2 | Servo Savox | PWM 50 Hz en GP15 → dirección Ackermann |
| ToF VL53L4CD ×2 | Pico Plus 2 | I²C vía Qwiic MultiPort, reservados para parking Reto 2 |
| Botón físico (GP28) | Pico Plus 2 → RPi 5 | Publica /start → control captura section_angle al arrancar |

## 7c. Restricciones (Constraints) Identificadas

| Restricción | Límite | Impacto en el diseño |
|---|---|---|
| Dimensiones máximas | 300 × 200 × 300 mm (regla WRO 2026) | Llevó a chasis personalizado 230×150×126 mm |
| Peso máximo | 1500 g | El robot final pesa 1.100 g (margen +400 g) |
| Altura paredes pista | 10 cm | Forzó LiDAR al primer piso adelantado para barrer a la altura correcta |
| Altura pilares (Reto 2) | ~10 cm coloreados R/G | Forzó lente CCTV 2.8 mm (FoV 96°) y angulo de 60° para capturar pilares cercanos |
| FoV útil del LiDAR | Solo 193°–350° (157° hacia adelante) | Todos los sectores del control deben estar dentro de ese rango |
| Voltaje mínimo bus motor | 12 V nominal | Forzó LiPo 3S (2S no era suficiente) |
| Pico de corriente servo | hasta 3.5 A | Forzó regulador 5V dedicado al servo (D36V50F5) |
| Sin Wi-Fi en la pista | 0 conectividad | Arranque autónomo vía systemd + botón físico |
| Tiempo de boot | ~40 s | Aceptado: priorizamos estabilidad sobre velocidad |

## 7d. Decisiones de Diseño Principales

Esta subsección resume las decisiones de ingeniería más importantes con su razonamiento. 
**Cada decisión sigue el patrón "elegimos X en vez de Y porque…"** Aunque la comparativa de componentes se hará en el **Engineering Journal, sección 7**.

### Decisión 1 — Arquitectura: RPi 5 como Cerebro + Pico 2 como ejecutor y reportador de datos 

| Opciones consideradas | Veredicto |
|---|---|
| **A: Toda la lógica en RPi 5, Pico solo sensores y actuadores** | ✓ **Elegida** |
| B: Lógica distribuida (RPi 5 alto nivel, Pico control local) | Descartada |
| C: Todo en Pico, sin Pi 5 | Descartada |

**Por qué A:** Python en la RPi 5 acelera la iteración de algoritmos
(ROS 2, OpenCV); el Pico ofrece tiempo real estricto para encoder e
IMU; la frontera entre los dos es un protocolo CSV legible. **El
Pico es deliberadamente ejecutor:** no decide, solo ejecuta.

### Decisión 2 — Lógica del Reto Abierto: 4 pilares en lugar de máquina de estados compleja

| Pilares | Función |
|---|---|
| **Pilar 1** | Localización (odometría) y conteo de **12 giros** (interpretación más robusta) |
| **Pilar 2** | Detección de esquinas (mediana frontal + confirmación lateral + debounce espacial) |
| **Pilar 3** | Control en 3 capas (heading, wall-centering, velocidad adaptativa) |
| **Pilar 4** | Fin de carrera con banda de parada 1,2 a 1,5m |

**Por qué 4 pilares y no máquina de estados grande:** la máquina se reduce a solo 5 estados (`BOOT → READY → RUNNING → FINISH_APPROACH → STOPPED`); el resto de la complejidad vive como capas dentro del estado `RUNNING`, fácil de ajustar capa por capa sin tocar las otras.

### Decisión 3 — Reto con Obstáculos: Siguiendo Camino de 3 capas

| Capa | Función | Sensor principal |
|---|---|---|
| **Capa 1 — Ruta Proyectada** | Ray marching para encontrar la mejor dirección libre | LiDAR |
| **Capa 2 — Recorte por color** | Rutas posibles se limitan según color del pilar (rojo→derecha, verde→izquierda) | Cámara |
| **Capa 3 — SpiderSense** | Reflejo lateral de emergencia si un pilar o pared se acerca demasiado | LiDAR |

**Por qué navegación reactiva y no detección de eventos:** la busqueda de ruta más profunda maneja curvas y pilares implícitamente, sin la necesidad de "detección
de esquina, que es mas dificil en la presencia de obstaculos. La cámara es solo semáforo de color (rojo/verde), no estima distancia. La distancia la lleva el LiDAR.

### Decisión 4 — Conteo de vueltas por yaw acumulado, no por esquinas

**Por qué |acc_yaw| > 900° en Reto 2** (en lugar de contar giros como en Reto 1): los pilares fuerzan trayectorias no rectangulares; el robot puede "girar" 90° por una curva *o* por una evasión, y
contar esquinas confundiría ambas. El yaw acumulado es robusto en ambos casos. Solo hay que configurar bien el color Magenta.

### Decisión 5 — Detección de sentido CW/CCW en la primera esquina

**Antes:** intentábamos detectar sentido con discontinuidades del LiDAR antes de arrancar (robot quieto).
**Problema:** en pruebas no funcionaba consistentemente.
**Decisión:** adoptar enfoque de esperar a la primera esquina y elegir el lado con apertura.
**Resultado:** robusto, se eliminó un estado `DETECTING_SENSE` que estaba presente en una versión inicial del Reto 1.

## 7.e Análisis de Riesgos y Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación implementada |
|---|---|---|---|
| Caída del riel 5V por pico del servo | **Alto** | Reset de la RPi 5 a mitad de carrera | **Regulador dedicado al servo** (D36V50F5) |
| EMI del motor sobre IMU | Media | Yaw inestable | IMU en piso superior + canales de cable separados |
| LiDAR no ve paredes de 10 cm | **Alta si mal montado** | Imposibilidad de centrarse | **LiDAR en primer piso, no en piso superior** |
| ToF lee basura a <15 mm | Media | Lecturas espurias en parking | Sensor retraído ≥15 mm + filtro software |
| Cámara sin rolling shutter distorsiona | Media | Falsos positivos de pilar | Global shutter elegida específicamente |
| Variación de iluminación en pista | Alta | Falla detección de color | Calibración HSV in-situ con `calibrador_hsv.py` |
| Pérdida de comunicación Pi ↔ Pico | Baja | Robot fuera de control | Reconexión USB automática en bridge |
| Robot atascado contra pared | Media | Pérdida de la ronda | SpiderSense reflejo lateral (Capa 3 Reto 2) |


## 7.f Historial de Iteraciones (resumen)

| Versión | Cambio principal | Resultado |
|---|---|---|
| **V0.1** | Diseño inicial 3 pisos, motor 20.4:1, batería 2S, LiDAR arriba, 1 sólo regulador | Demasiado alto, potencia insuficiente, LiDAR no ve paredes bajas o montarlo volteado como algunos equipos |
| **V1.0** | Rediseño chasis 2 pisos + compartimiento de batería, motor 34:1, batería 3S, servo Savox SC-1251MG digital, LiDAR abajo y adelante + 2 reguladores | Geometría compacta, Ackermann real, LiDAR ve paredes, Mejor distribucción de energía |
| **V2.0** | Compartimiento de batería y repisa, generaron un subnivel para ubicar IMU y botón de arranque, asi como mejorar cableado| Sistema robusto, cableado limpio, sin necesidad de 3er Nivel **✓** |
| **Reto Abierto V1** | 4 pilares con detección de sentido pre-arranque | No funcionaba consistentemente |
| **Reto Abierto V2** | Detección de Sentido por 1era Esquina, Reducción de Velocidad y Ajuste del P Control  | Estabilidad y Alta Tasa de Ëxito del Reto Abierto **✓** |
| **Reto con Obstaculos V1** | Gap follower de 3 capas "Siguiendo Camino-RecortexColor y SpiderSense" | Aún en ajustes, con cambios en parametros y velocidad para dar mas tiempo de respuesta  |

# 8. Instrucciones de Reproducibilidad (Criterio 5)

 Esta sección permite que **otro equipo pueda replicar el robot **Proyecto Mahoraga** desde cero. Incluye lista de hardware con links de compra, requisitos de software, instalación paso a paso, estructura del repositorio, archivos CAD/3D y procedimiento de arranque en
competencia. Sin embargo, el emsamblaje y el paso a paso estará aún más detallado en el **_Engineering Journal Sección 8_**.

## 8.a Requisitos de Hardware

Para facilitar su reproductibilidad anexamos lista completa de los componentes con los enlaces de compra de cada componente.<br>

| Categoría | Componente | Modelo / SKU | Cant. | Link |
|---|---|---|---|---|
| **Cómputo** | SBC alto nivel | Raspberry Pi 5 — 16 GB RAM | 1 | [Adafruit 6125](https://www.adafruit.com/product/6125) |
| | Refrigeración | Official Raspberry Pi 5 Active Cooler | 1 | [Adafruit 5815](https://www.adafruit.com/product/5815) |
| | Base NVMe | Pimoroni NVMe Base PIM699 | 1 | [Adafruit 5845](https://www.adafruit.com/product/5845) |
| | SSD | Silicon Power 128 GB M.2 NVMe Gen3 | 1 | Amazon |
| | MicroSD (backup) | Silicon Power 32 GB | 1 | Amazon |
| | Microcontrolador | Pimoroni Pico Plus 2 (RP2350) PIM724 | 1 | [Adafruit 6244](https://www.adafruit.com/product/6244) |
| | Adapter terminal | Adafruit Terminal PiCowbell con sockets | 1 | [Adafruit 5907](https://www.adafruit.com/product/5907) |
| **Sensores** | LiDAR 360° | LDROBOT STL-27L (25 m) | 1 | [DFRobot 2726](https://www.dfrobot.com/product-2726.html) |
| | Cámara | Raspberry Pi Global Shutter (IMX296) | 1 | [Adafruit 5702](https://www.adafruit.com/product/5702) |
| | Lente cámara | CCTV M12 2.8 mm F2.0 1/2.7" | 1 | Amazon |
| | Cable cámara | FPC 22-pin → 15-pin, 200 mm (RPi 5) | 1 | [Adafruit 5818](https://www.adafruit.com/product/5818) |
| | ToF láser | Adafruit VL53L4CD STEMMA QT | 2 | [Adafruit 5396](https://www.adafruit.com/product/5396) |
| | IMU 9-DOF | Adafruit BNO085 STEMMA QT | 1 | [Adafruit 4754](https://www.adafruit.com/product/4754) |
| | Concentrador I²C | SparkFun Qwiic MultiPort | 1 | [SparkFun](https://www.sparkfun.com/sparkfun-qwiic-multiport.html) |
| | Cable Qwiic | Flexible Qwiic Cable 50 mm | 4 | [SparkFun](https://www.sparkfun.com/flexible-qwiic-cable-50mm.html) |
| **Actuadores** | Motor + encoder | Pololu 34:1 25Dx67L MP 12V + encoder 48 CPR | 1 | [Pololu 4864](https://www.pololu.com/product/4864) |
| | Driver de motor | Pololu VNH5019 Motor Driver Carrier | 1 | [Pololu 1451](https://www.pololu.com/product/1451) |
| | Servo de dirección | Savox SC-1251MG digital coreless | 1 | [Savox](https://savox-servo.com/en/product/SC-1251MGplus/savox-servo-sc-1251mg-digital-coreless-motor-metal-gear) |
| **Potencia** | Batería | Zeee LiPo 3S 11.1 V 3200 mAh 50C | 1 | [Zeee Battery](https://zeeebattery.com/collections/zeee-3s-lipo-battery/products/zeee-3s-lipo-battery-3200mah-11-1v-50c-deans-t) |
| | Regulador 5V — Lógica | Pololu D24V90F5 (5 V, 9 A) | 1 | [Pololu 2866](https://www.pololu.com/product/2866) |
| | Regulador 5V — Servo | Pololu D36V50F5 (5 V, 5.5 A) | 1 | [Pololu 4091](https://www.pololu.com/product/4091) |
| **Mecánica** | Ruedas | 64 mm aluminio + neumático goma | 4 | Amazon |
| | Eje trasero | KYX Racing Steel Drive Shaft (Tamiya DT04) | 1 | Amazon |
| | Manguetas Ackermann | KYX Racing Aluminum Steering Knuckles | 2 | Amazon |
| | Servo saver | Tamiya TT-02 Hi-Torque | 1 | [Tamiya](https://www.tamiyausa.com/). |
| | Tie rods | M3 ajustables uxcell | 2 | Amazon |
| | Ejes | Acero inoxidable 5 mm × 100 mm uxcell | 2 | Amazon |
| **Cables** | USB-C Pi↔Pico | SUNGUY USB-C 3.1 Gen2 — 6 in y 1 ft | 2 | Amazon |
| **Mecánica 3D** | Filamento | PLA Bambu Lab | — | Bambu Lab |
| | Impresora 3D | Bambu Lab P2S | — | Bambu Lab |

**Listado de impresiones 3D** 

Se realizó un Anexo de la Sección 8.1. dedicado a las Piezas 3D, su distintas evoluciones, fotos de su prototipo, versiones en 3D y Foto del componente ya impreso. El anexo está disponible [**/materials/Piezas 3D.md**](https://github.com/NPC2team/NPC2-WRO-team-2026/blob/main/materials/Piezas%203D.md)

Los componentes impresos en 3D tienen sus archivos en STL/3MF en **/models.** 

||Formato|Formato|
|---|---|---|
|Pieza|3mf|STL|
|Canal 2 Cables Tapa|x|x|
|Canal 3 Cables Tapa|x|x|
|Canal 4 Cables Tapa|x|x|
|Canal 2 Cables|x|x|
|Canal 3 Cables|x|x|
|Canal 4 Cables|x|x|
|Chasis Abajo V2|x|x|
|Chasis Arriba V2|x|x|
|Espaciador de Eje|x|x|
|Gear Box Diferencial|x|x|
|Gear Diferencial|x|x|
|Gear Motor con<br>Flange|x|x|
|Repisa|x|x|
|Soporte Motor VF|x|x|
|Soporte Servo VF|x|x|
|Sujetador de Cables|x|x|

### Configuración de impresión recomendada

```
Material:    PLA Bambu Lab
Boquilla:    0.4 mm
Capa:        0.2 mm
Perímetros:  3
Infill:      25 % (55 % para Chasis)
Soportes:    Sí - Tipo árbol
Impresora:   Bambu Lab P2S
```

## 8.b Requisitos de Software

### En la Raspberry Pi 5

```
- Ubuntu 24.04 LTS (Server, no Desktop, para arranque rápido)
- ROS 2 Jazzy Jalisco
- Python 3.12
- OpenCV 4.x (apt install python3-opencv)
- Driver oficial LDROBOT ldlidar_stl_ros2
- Workspace npc_ws con paquetes npc_bot y npc_interfaces
- systemd service npc_bot.service (auto-arranque)
```

### En la laptop de desarrollo

```
- Ubuntu 24.04 LTS (Desktop, en nustro caso hicimos una partición separada a Windows)
- Arduino IDE 2.3.8
- Board package: Earle Philhower RP2350 (para Pico Plus 2)
- Librerías Arduino: Adafruit BNO08x, SparkFun VL53L4CD
- Visual Studio Code
- Autodesk Fusion 360 (CAD)
- Bambu Studio (laminado e impresión)
- Git
```

## 8.c Instalación Paso a Paso

### 1) Preparar la Raspberry Pi 5

```bash
# Sistema operativo Ubuntu 24.04
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-opencv python3-numpy python3-pip

# ROS 2 Jazzy Jalisco
# https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html
sudo apt install -y ros-jazzy-desktop ros-jazzy-cv-bridge
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

### 2) Workspace LiDAR

```bash
mkdir -p ~/lidar_ws/src && cd ~/lidar_ws/src
git clone https://github.com/ldrobotSensorTeam/ldlidar_stl_ros2.git
cd ~/lidar_ws
colcon build
echo "source ~/lidar_ws/install/setup.bash" >> ~/.bashrc
```

### 3) Workspace de la cámara (camera_ros)

```bash
mkdir -p ~/camera_ws/src && cd ~/camera_ws/src
git clone https://github.com/christianrauch/camera_ros.git
cd ~/camera_ws
colcon build
echo "source ~/camera_ws/install/setup.bash" >> ~/.bashrc
```

### 4) Workspace principal (npc_bot)

```bash
mkdir -p ~/wro_ws/src && cd ~/wro_ws/src
git clone https://github.com/[equipo-NPC]/wro2026-future-engineers.git npc_bot
cd ~/wro_ws
colcon build
echo "source ~/wro_ws/install/setup.bash" >> ~/.bashrc
```

### 5) Cargar firmware al Pico Plus 2

```
1. Conectar Pico Plus 2 vía USB a la laptop
2. Abrir src/firmware/pico_firmware.ino en Arduino IDE 2.3.8
3. Seleccionar Board: "Pimoroni Pico Plus 2 (RP2350)"
4. Seleccionar puerto serial correcto
5. Click Subir (Upload)
```

### 6) Calibración HSV de la cámara (Reto 2)

 Interfaz interactiva con sliders para calibrar rangos HSV de rojo, verde y magenta. 

```bash
ros2 run npc_bot calibrador_hsv
```

### 7) Servicio systemd (auto-arranque, requerido por reglas WRO 9.6–9.14)

```bash
sudo cp src/systemd/npc_bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable npc_bot.service
sudo systemctl start npc_bot.service
```

Tiempo de boot hasta robot listo: **~40 segundos** desde encendido al pitido de "READY".

## 8.d Estructura del Repositorio

```
/
├── README.md                  ← este documento (índice maestro)
├── LICENSE
├── journal/                   ← Engineering Journal (extendido)
│   ├── README.md
│   
├── src/                       ← código fuente
│   ├── firmware/
│   │   └── pico_firmware.ino  ← firmware Pico Plus 2 (Arduino)
│   ├── npc_bot/               ← paquete ROS 2 Python
│   │   ├── pico_bridge_node.py
│   │   ├── control_node.py             (Reto 1 — Open Challenge)
│   │   ├── control_node_reto2.py       (Reto 2 — Obstacle Challenge)
│   │   ├── nodo_camara.py              (visión Reto 2)
│   │   └── calibrador_hsv.py           (calibración interactiva)
│   ├── npc_interfaces/        ← paquete ROS 2 con mensajes custom
│   │   └── msg/NpcPose.msg    ← {x, y, theta, acc_yaw}
│   ├── launch/                ← launch files
│   │   ├── npc_bot.launch.py           (Reto 1)
│   │   └── base_reto2.launch.py        (Reto 2)
│   └── systemd/
│       └── npc_bot.service    ← arranque automático
├── models/                    ← archivos CAD/3D
│   ├── *.stl                  ← geometría imprimible
│   ├── *.3mf                  ← proyectos Bambu Studio
│   └── *.step                 ← modelos (motor Pololu)
├── schemes/                   ← diagramas eléctricos
│   ├── conexiones-del-robot.pdf
│   └── diagrams/
│       ├── wiring.png
│       ├── mechanical.png
│       └── system_overview.png
├── t-photos/                  ← fotos del equipo
│   
├── v-photos/                  ← fotos del vehículo (6 ángulos)
│   ├── front.jpg
│   ├── back.jpg
│   ├── left.jpg
│   ├── right.jpg
│   ├── top.jpg
│   └── bottom.jpg
└── video/
    └── video.md               ← link a video de demostración (YouTube)
```

## 8.e Cómo Arrancar el Sistema

### Opción A — Arranque automático (En competencia)

```
1. Conectar batería LiPo 3S
2. Encender interruptor principal
3. Esperar ~40 s (LED indicador en verde fijo = listo)
4. Colocar robot en la pista en posición de salida
5. Presionar botón físico (GP28) → el robot captura section_angle
   y arranca la lógica de carrera
```

### Opción B — Arranque manual (En prácticas para depuración)

Terminal 1 — LiDAR:
```bash
ros2 launch ldlidar_stl_ros2 stl27l.launch.py
```

Terminal 2 — Bridge del Pico:
```bash
ros2 run npc_bot pico_bridge
```

Terminal 3 — Control (elegir uno según el reto):
```bash
ros2 run npc_bot control_node           # Reto 1: Open Challenge
ros2 run npc_bot control_node_reto2     # Reto 2: Obstacle Challenge
```

Terminal 4 (solo Reto 2) — Cámara + visión:
```bash
ros2 launch npc_bot base_reto2.launch.py
```


## 8.f Notas de Ensamblaje


Resumen del orden recomendado:

1.  Imprimir todas las piezas
2.  Ensamblar diferencial: insertar engranajes cónicos en `Gear Box Diferencial`
3.  Montar eje trasero KYX con diferencial en el `Chasis Abajo` ajustando con sus Sortes y Espaciadores.
5.  Montar Motor Pololu 34:1 con `Soporte Motor` y `Gear Motor con Flange`
6.  Montar servo Savox detrás de las ruedas delanteras en su `Soporte Servo VF`
7.  Conectar manguetas KYX + tie rods M3 + servo saver Tamiya
8.  Ajustar alineación con servo centrado
9.  Colocación del LiDAR STL27L
10. Colocar Soportes y Chasis de Arriba
11. Montar VNH5019, reguladores con batería LiPO S3 en el primer piso
12. Montar Raspberry Pi 5 y Pico Plus 2
13. Colocación de Sensores TOF e IMU + Botón de Inicio
14. Ruteo de cables por los canales modulares y agujeros del Chasis 
15. Colocación de Cámara

<table>
  <tr>
    <td align="center">
      <b>Ensamble del Diferencial</b><br>
      <img width="960" height="1280" alt="01 Diferencial con Soporte" src="https://github.com/user-attachments/assets/6e5646f1-0f24-48be-b2f5-8573089c3192" />
    </td>
    <td align="center">
      <b>Soportes del Diferencial + Ruedas</b><br>
      <img width="960" height="1280" alt="02 Diferencial con Ruedas" src="https://github.com/user-attachments/assets/f1fe4b57-816f-43ad-9fba-1a12d8b0aa38" />
    </td>
    <td align="center">
      <b>Montaje del Motor</b><br>
      <img width="960" height="1280" alt="03 Motor" src="https://github.com/user-attachments/assets/b26effcc-1b17-4a2a-98c8-e82fbcee9ebe" />
    </td>
  </tr>
   <tr>
    <td align="center">
      El diferencial va ajustado en el espacio considerado en el chasis para él, colocando los primeros soportes y los espaciadores hechos a la medida para garantizar que la caja del diferencial no se deslice de lado cuando gire el motor<br>
    </td>
    <td align="center">
      El otro par de soportes se incluyen para evitar que no quede recto la transmisión, como pasaba en la versión anterior del Chasis por el peso de la caja del diferencial. Se ajustan las ruedas y se revisa que queden bien sujetas y a la misma distancia del chasis a cada lado.<br>
    </td>
    <td align="center">
      Los agujeros del chasis garantizan que el soporte del motor quede ubicado donde los engranajes del motor y del diferencial estan alineados. Importante que el nuevo enganaje del Motor impreso en Nylon, permite a diferencia del PLA utilizado antes mayor resistencia a la fricción.<br>
    </td>
  </tr>
   <tr>
    <td align="center">
      <b>Montaje de Dirección</b><br>
      <img width="791" height="964" alt="05 Servo" src="https://github.com/user-attachments/assets/f63274ec-be18-4463-8ca0-09d9c5613019" />
    </td>
  <td align="center">
  <b>Colocación del LiDAR</b><br>
  <img width="907" height="1137" alt="06 LiDAR" src="https://github.com/user-attachments/assets/2f99dec4-c244-4012-81f6-0559b57d0ed7" />
</td>
    <td align="center">
      <b>Colocación del Chasis Superior</b><br>
      <img width="824" height="667" alt="08 Chasis Arriba" src="https://github.com/user-attachments/assets/8e4b45b6-1c51-4d72-a92e-ddffc996772b" />
    </td>
  </tr>
<tr>
    <td align="center">
     Las barras se atornillan a las manguetas y estas a las C-Hubs del chasis. Las tierods son ajustables para lograr la alineación con el centro del servo. El soporte del servo se fija al chasis y se atornilla el tierod al Servo Saver. Para armar el Servo Saver, dejamos un <a href="https://www.youtube.com/watch?v=pzWLF9ScBSY" target="_blank">Link</a> que nos ayudó. <br>
    </td>
    <td align="center">
      El LiDAR se atornilla en la parte frontal asegurando que quede fijo y garantice un Field of View de 180 grados. <br>
    </td>
    <td align="center">
      Los agujeros del chasis superior e inferior estan alineados para colocar los soportes de 6cms y así unir ambos chasis, garantizando el espacio con holgura para que los componentes y el subnivel de la bateria entren sin problema.<br>
    </td>
  </tr>
</table>
---
<table>
  <tr>
    <td align="center">
      <b>Colocación de Driver del Motor y Regulador</b><br>
      <img width="960" height="1280" alt="09 VNH + Reg" src="https://github.com/user-attachments/assets/97845b76-bd8d-4c42-a3a6-7559b54dd561" />
    </td>
    <td align="center">
      <b>Regulador del Servo</b><br>
      <img width="960" height="1280" alt="10 Conexion Reg Servo" src="https://github.com/user-attachments/assets/94fdc828-db87-4f66-832b-b3845d0c0dce" />
    </td>
    <td align="center">
      <b>Colocación de Pico 2 Plus</b><br>
      <img width="864" height="1220" alt="15 Conexion Pico 2 Plus" src="https://github.com/user-attachments/assets/5ff79966-f1cc-4f6d-93f1-813cb2b64b93" />
    </td>
  </tr>
  <tr>
    <td align="center">
     Continuamos con la parte eléctrica, colocando el VNH5019 y el Regulador Cenral que reciben energía de la batería a través del switche de encendido. Para el detalle del cableado ver la sección 5 del Readme o del Journal. <br>
    </td>
    <td align="center">
      Arriba en la parte frontal ubicamos el regulador D36V50F5, encargado exclusivamente del servo. Recibe la energía a través del switche y la envía al Servo. Pasamos los cables por los agujeros del chasis para conectar con el sevo qque está abajo. Para asegurar los cables Dupont utilizamos un sujetador.<br>
    </td>
    <td align="center">
      Encima del compartimiento de la batería ubicamos el Pico 2 Plus. Queda centrado en el vehículo, lo cual era importante porque es el que mas conexiones lleva (VNH5019, Encoder, Botón de Arranque, RPI5, IMU y TOF). <br>
    </td>
  </tr>
   <tr>
    <td align="center">
      <b>Colocación de RPI 5</b><br>
      <img width="860" height="1067" alt="131 RPI5" src="https://github.com/user-attachments/assets/0953eb00-98e1-4551-b401-8a099996a491" />
    </td>
  <td align="center">
  <b>Botón + IMU BNO085</b><br>
  <img width="960" height="1036" alt="16 IMU + Boton" src="https://github.com/user-attachments/assets/e9ccc935-7b76-45bb-986b-214debf63de6" />
</td>
    <td align="center">
      <b>Foto Final</b><br>
      <img width="824" height="667" alt="08 Chasis Arriba" src="https://github.com/user-attachments/assets/8e4b45b6-1c51-4d72-a92e-ddffc996772b" />
    </td>
  </tr>
   <tr>
    <td align="center">
     La RPI5 la ubicamos en la parte trasera y sus conexiones principales son con el Pico 2 Plus y el LiDAR, como la comunicación es por USB es importante tener cables muy cercanos a la medida necesaria. Para armar el NVME segimos el paso a paso de la pagina oficial de <a href="https://learn.pimoroni.com/article/getting-started-with-nvme-base?gad_source=1&gad_campaignid=21808011029&gbraid=0AAAAADqO9eI2JBt_V5J718nZPukufdGr8&gclid=CjwKCAjwu53SBhAhEiwAJzSLNn-C14eCdenwd9VDtsrBGij-e7OjglkBVuX8pjsKX0_WzyU9FhXqaRoC4g8QAvD_BwE" target="_blank">Pimoroni</a>. <br>
    </td>
    <td align="center">
      Al lado del Pico 2 Plus, colocamos una protoboard y ahi encajamos el Botón de Inicio y el IMU BNO085, asegurandonos que no utilicen las misma lineas de conexión. Si bien el IMU se conecta por Qwiic los pines pueden interferir.<br>
    </td>
    <td align="center">
      Colocación de la Cámara en su soporte en el Piso de Arriba y <b>Proyecto Mahoraga</b> queda totalmente armado y listo luego de ajustar cableado (Sección 5) y la programación (Sección 6 y 7).<br>
    </td>
  </tr>
</table>
