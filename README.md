
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

- d. Lista de Componentes 

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

- b. Tópicos 

- c. Firmware del Pico 2 

- d. Estrategia del Reto Abierto

- e. Métricas de Desempeño del Reto Abierto 

- f. Ajustes Realizados 

## **1.Encabezado e Información del Equipo** 

## 1a. Introducción 
<div>
<img width="316" height="411" align="left" alt="Equipo" src="https://github.com/user-attachments/assets/75947953-eac8-472f-b4b6-771bddc59407" /><br>
   
Somos el equipo **NPC (Non Playable Character)**, este es nuestro segundo año en competencias de la WRO, con el objetivo de lograr un vehículo verdaderamente autónomo que supere con éxito los retos de la competencia WRO    Futuros Ingenieros 2026 a Nivel Nacional y nos permita obtener nuestro cupo en la Final Internacional de Puerto Rico. 

Vu Tue Anh, compitió el año pasado en la categoría de misiones roboticas, mientras que Leonardo y Juan participaron en la categoría de futuros ingenieros, llegando a la Final Nacional de Venezuela donde obtuvimos el 5to Lugar, mientras que en un invitacional en Weifang, China donde logramos el 1er Lugar. 
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

**“Proyecto Mahoraga”** es nuestro vehículo para Futuros Ingenieros 2026, representa una evolución significativa con respecto a **“Crazy Diamond” (WRO 2025)**, con quien ya logramos triunfos y a quien le agradecemos el aprendizaje. Proyecto Mahoraga presenta mejoras en hardware, diseño y software que nos permitirá abordar con éxito los retos de Futuros Ingenieros 2026. Abordaremos con detalle en este Readme y en el Engineering Journal las características del Robot, el proceso de diseño, construcción y programación, así como las decisiones y obstáculos que tuvimos en el camino, con la finalidad de que sea posible replicar por cualquier entusiasta de la robótica como nosotros. 

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

## **3.Videos de Pruebas del Vehículo** 

3a. Reto 1 – Open Challenge 

**Link YouTube** 
(https://youtube.com/shorts/lqm2GCjuBmU?feature=share)

3b. Reto 2 – Obstacle Challenge 

**Link YouTube** 

## **4.Movilidad y Diseño Mecánico (Criterio 1)** 

En este apartado documentamos la ficha técnica de la configuración mecánica final de Proyecto  Mahoraga.  En  el  Engineering  Journal  (Sección  4)  incluimos  la  descripción completa  del proceso  de  diseño,  las  mejoras sobre  nuestro  robot 2025,  los ajustes realizados sobre la versión inicial de Proyecto Mahoraga y los cálculos detallados del Ackerman, torque y velocidad. 

## 4a. Chasis 

Compuesto por 2 niveles, con un subnivel adicional y un compartimiento hecho a la medida para la batería Lipo S3 11.1V. Esto con la finalidad de hacer más eficiente el uso del espacio y lograr obtener un robot más pequeño y ágil. Las piezas fueron impresas en 3D, dándonos mayor flexibilidad en el diseño y permitiéndonos adecuar los espacios a los componentes mecánicos y eléctricos de Proyecto Mahoraga. 

<img width="604" height="426" alt="Chasis Comentado" src="https://github.com/user-attachments/assets/6b80a166-bae0-440d-9ea4-06bb7c6f8add" />



|**Atributo**|**Descripción**|
|---|---|
|Tipo|Personalizado, diseñado en Fusion|
|Material|PLA impreso en 3D(Bambu Lab P2S)|
|Dimensiones|205 × 135 × 126 mm|
|Distribución vertical|2pisos modulares + subnivel|
|Distancia entre ejes(batalla)|142 mm|
|Distancia entrepivotes|97 mm|
|Peso(sin cámara)|1.100g (límite reglamentario: 1500g)|



Todos los archivos en STL/3MF están en **/models** (chasis de abajo y de arriba, soportes de motor y servo, carcasa y engranajes del diferencial y motor, espaciadores, repisa, canales de cables con tapas). 

En el Engineering Journal en la sección 4.1 comentamos la evolución del chasis luego de un proceso iterativo, así como su comparativo con la versión que manejamos en 2025. 

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
|Torque|1,65 Kg/cm(Sin Diferencial)2,32 Kg/cm(Con Diferencial)|
|Resolución calibrada|2.006 ticks/metro(medido enpruebas)|
|Driver del Motor|Pololu VNH5019 Tecnología MOSFET|
|Diferencial|Impreso 3D propio (Gear Diferencial + Gear Box)|
|Eje trasero|KYX Racing acero (compatible Tamiya DT04)|
|Ruedas|64 mm aluminio, ancho 11 mm + neumático de goma|



En el Engineering Journal en la sección 4.2 comentamos porque elegimos estos componentes y la comparativa con otras opciones, adicionalmente detallamos el cálculo de ticks por metro del encoder, la velocidad lineal y el torque del motor. 

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



_En el Engineering Journal en la sección 4.3 describimos más ampliamente los componentes de la dirección, las ventajas del principio Ackerman, así como los cálculos para obtener el radio de giro y la distancia necesaria para completar un giro de 90 grados. Comparamos estos resultados con los que obtuvimos en el 2025 y explicamos las mejoras._ 

## 4d. Lista de Componentes 

Para facilitar su reproductibilidad anexamos lista completa de los componentes. Todos los enlaces de compra de cada componente: ver ./lista-componentes.md. Los archivos en STL/3MF están en **/models.** 

|**Componente**|
|---|
|Raspberry Pi 5 - 16 GB RAM Official Raspberry Pi 5|
|Official Raspberry Pi 5 Active Cooler| 
|Pimoroni NVMe Base for Raspberry Pi 5|
|Silicon Power 128GB NVMe M.2 PCIe Gen3x4 2280 SSD|
|Silicon Power 32GB 3D NAND High Speed MicroSD Card with Adapter|
|Pimoroni Pico Plus 2 - RP2350 Dev Board with Pico Shape and Pins - PIM724| 
|Adafruit Terminal PiCowbell for Pico with Reset Button & STEMMA QT|
|LDROBOT STL-27L| 
|Raspberry Pi Global Shutter Camera|
|1080P CCTV Lens 2.8mm  M12 Mount 2MP Aperture F2.0 1/2.7 Format for Camera|
|Raspberry Pi 5 FPC Camera Cable - 22-pin 0.5mm to 15-pin 1mm - 200mm long|
|Adafruit VL53L4CD Time of Flight Distance Sensor - ~1 to 1300mm - STEMMA QT / Qwiic|
|Adafruit 9-DOF Orientation IMU Fusion Breakout - BNO085 - STEMMA QT / Qwiic|
|34:1 Metal Gearmotor 25Dx67L mm MP 12V with 48 CPR Encoder|
|VNH5019 Motor Driver Carrier|
|Savox SC-1251MG Be Coreless Motor Metal Gear|
|5V, 5.5A Step Down Voltage Regulator D36V50F5|
|Pololu 5V, 9A Step Down Voltage Regulator D24V90F5|
|Batería: LiPo 3S (11.1V) - 3200mAh|
|64mm Metal Drive Wheel Inner Dia 6mm Aluminum Rubber Tires|
|SparkFun Qwiic MultiPort|
|Flexible Qwiic Cable - 50mm|
|SUNGUY 10Gbps USB Cable 6 inch, 3A USB C 3.1 Gen2 Cable Data Transfer, USB C|
|SUNGUY 10Gbps USB Cable 1FT, 3A USB C 3.1 Gen2 Cable Data Transfer, USB C|
|KYX Racing Hard Steel Freewheel Axle Front Drive Shaft for 1/10 Rc Crawler Tamiya DT04|
|uxcell 5mm x 100mm 304 Stainless Steel Solid Round Rod for DIY Craft|
|uxcell M3 3.0xL15mm Lever Steering Linkage Tie Rod End Ball Head End for RC|
|uxcell M3x30mm Pushrod Connector Stainless Steel Rod Linkage|
|Tamiya TT-02 Hi-Torque Servo Saver Set|
|KYX Racing Aluminum Front Steering Knuckles for 1/10 Rc Crawler Tamiya DT04| 

 **Listado de impresiones 3D** 

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
|Sujetador de Cables|x|x|<img width="845" height="634" alt="Traccion" src="https://github.com/user-attachments/assets/cc327e21-5dd0-40a2-a66e-4c440b1b4139" />


## **5. Arquitectura de Potencia y Sensores (Criterio 2)** 

En este apartado documentamos la ficha técnica del sistema de alimentación, distribución de potencia y arquitectura de sensores para Proyecto Mahoraga. 

_En el Engineering Journal (sección 5) se encuentran las justificaciones de selección de los componentes batería/reguladores, diagramas de cableado completos y presupuesto de energía (power Budget), así como justificación de selección de sensores y su proceso de calibración._ 

## 5a. Sistema de Potencia 

|**Componente**|**Modelo**|**Especificaciones**|
|---|---|---|
|Batería|Zeee LiPo 3S|11.1 V nominal, 3.200 mAh, 50C, conector T|
|Regulador Principal<br>(lógica)|Pololu D24V90F5|5V salida, 9 A continuos|
|Regulador  Servo|Pololu D36V50F5|5V salida, 5.5 A continuos|



La bateria 3S nos permite alimentar correctamente el motor Pololu 34:1 25Dx67L MP 12V y sacar provecho de su potencia. 

**Decisión clave:** Distribución dual de reguladores 5V. El D24V90F5 (9A) alimenta toda la lógica del robot (Raspberry Pi 5, Pico Plus 2, LiDAR, IMU, TOF, lógica del VNH5019). El D36V50F5 (5.5A) alimenta exclusivamente el servo Savox SC-1251MG, que tiene picos de corriente durante giros bruscos o choques. Esto aísla los transitorios del servo del riel de lógica sensible, evitando reinicios del Raspberry Pi 5 o del Pico Plus 2. 

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

Uno de los upgrades más importantes que hicimos en Proyecto Mahoraga fue tener sensores de alto nivel. El LiDAR era una adición necesaria para el manejo de los obstáculos de una manera robusta. La ubicación y control preciso de los movimientos del robot queda cubierta con el IMU BNO085 y el Encoder. La cámara es un upgrade más profesional vs la Pixy que utilizamos en 2025 y los TOF VL53L4CD son un nivel más sofisticado que los ultrasónicos HC-SR04. 



|**Sensor**|**Modelo**|**Función**|
|---|---|---|
|LiDAR 360°|LDROBOT<br>STL-27L|Con 21.600 mediciones por segundo a 10 Hz (10<br>vueltas de 2.160 mediciones) es muy útil para la<br>detección de paredes y obstáculos.|
|IMU 9-DOF|Adafruit BNO085|Entrega orientación absoluta directamente como<br>quaternion, permitiendo una fácil orientación<br>absoluta.|
|ToF láser|Adafruit<br>VL53L4CD|Prácticamente sin punto ciego, distancia lateral<br>izq/der (1–1300 mm) a 100 Hz, es muy útil para<br>tareas de precisión como estacionar.|
|Cámara global<br>shutter|Raspberry Pi GS<br>Camera|Visión por computador para detectar pilares<br>rojos/verdes. Al ser Global Shutter limita las<br>distorsión de objetos en movimiento.|
|Lente|CCTV M12 2.8<br>mm F2.0|Campo de visión amplio para captura 96**°**|
|Encoder|Magnetic Encoder<br>Pololu|48 CPR motor, 2.006 ticks/m calibrados|

_En el Engineering Journal, sección 5.3 abordamos con detalle porque elegimos estos componentes._ 

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

_Diagrama completo de conexiones eléctricas: ver schemes/conexiones-del-robot.pdf._ 

_Detalle de cada conexión (pin a pin) en el_ _**Engineering Journal sección 5.5** ._ 

## **6. Arquitectura de Software y Estrategia de Obstáculos (Criterio 3)** 

## 6a. Visión General 

El software del robot **Proyecto Mahoraga** está construido sobre ROS 2 Jazzy corriendo en Ubuntu 24.04 en una Raspberry Pi 5 (16 GB), con un microcontrolador Pimoroni Pico Plus 2 (RP2350) encargándose de la lectura de sensores de bajo nivel y el control de actuadores. La arquitectura sigue un patrón distribuido de dos capas: 

• Raspberry Pi 5 (capa de alto nivel): ejecuta nodos ROS 2 para percepción, toma de decisiones y control a 40 Hz. 

• Pico Plus 2 (capa de bajo nivel): ejecuta un firmware basado en Arduino a mayor frecuencia para lectura del IMU, conteo del encoder, integración de odometría, generación de PWM del motor y del servo. 

La comunicación entre las dos capas ocurre por USB serial (921600 baudios) usando un protocolo CSV liviano, conectado a topicos ROS 2 mediante un nodo puente dedicado. 

<img width="612" height="474" alt="Nodos y Topicos Reto 1" src="https://github.com/user-attachments/assets/350644a9-b4a9-480d-b60c-c625360d443f" />


## 6b.Tópicos 

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



## 6c. Firmware del Pico 2 

El Pico Plus 2 ejecuta un firmware basado en Arduino (un único archivo.ino) que maneja todas las operaciones de tiempo real de las que la Pi5 no debe encargarse. 

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

## 6d.Estrategia del Reto Abierto 

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

Una vez que en la primera esquina se determina el sentido de los giros, en las siguientes esquinas el LiDAR, solo busca aperturas hacia esa dirección. 

<img width="593" height="168" alt="Pilar2" src="https://github.com/user-attachments/assets/61061769-7f22-4978-b0d0-93b03f1ba7d8" />

**Pilar 3. Control de Navegación y Centrado de Pared** 

Establecimos 2 esquemas de control de navegación: El Heading y el Centrado de Paredes donde el que tenga la corrección más importante tiene preferencia. Asi tenemos que: 

Heading: Una vez que el LiDAR detecta un desvío importante o detecto un cruce y se actualiza el nuevo ángulo destino +/-90° según sea la dirección, se produce un error alto que activa el heading y hace girar el servo. La agresividad del giro está controlada por un P-controller con dos ganancias diferenciadas. Una ganancia más agresiva (KP_Giro) cuando el error es superior a 15° y una ganancia menor (KP_Rect) cuando el error se reduce a 15°, esto hace que una vez que el error (desviación con el objetivo se reduce) el angulo de giro se suaviza evitando un sobrecruce o oscilaciones buscando el objetivo. 

<img width="589" height="119" alt="Pilar3" src="https://github.com/user-attachments/assets/9336211f-0aa3-47d7-ab3f-eba3bd153de3" />

Centrado de Paredes: Tal como va haciendo las mediciones para detectar las aperturas, también va realizando mediciones para calcular desviaciones respecto al centro de la pista 

<img width="588" height="31" alt="Pilar31" src="https://github.com/user-attachments/assets/39a1a01e-b639-493c-a92f-10774f70cd28" />

El algoritmo de centrado no actúa todo el tiempo; solo se activa si se cumplen estas tres condiciones simultáneamente:

<img width="594" height="43" alt="Pilar32" src="https://github.com/user-attachments/assets/339a9f8f-855c-434a-a0d3-14963a4e2048" />

Esto garantiza que no haya la medición de error cuando hay una apertura, que no se active el centrado cuando está girando o apenas lleva 40cms desde el último giro e interfiera en el giro.

<img width="591" height="29" alt="Pilar33" src="https://github.com/user-attachments/assets/51093f1b-f6c7-4e3a-ab0f-f768eda3fa56" />

Si las condiciones se cumplen, el código calcula cuánto debe corregir la dirección. 

Cálculo del error (pos): Resta la distancia derecha menos la izquierda. 

- Si el robot está perfectamente centrado, dist_der y dist_izq serán iguales, por lo que pos = 0 (no se necesita corrección). 

- Si el robot se arrima a la izquierda, dist_izq se reduce, haciendo que pos sea un valor positivo (orden de corregir hacia la derecha). 

Control Proporcional (Kp): Multiplica ese error por una constante de ganancia (KP_LATERAL). A mayor desviación, mayor será la fuerza del giro corrector, tal como hacíamos en el Heading con 2 Kp. 

Saturación (clamp): Limita el comando de dirección (str_lateral) entre -0.5 y +0.5 para evitar que un cálculo extremo haga que el robot derrape o pierda el control. 

El robot ya viene calculando el Heading (str_heading) apuntando hacia el angulo objetivo. El código compara las magnitudes absolutas del Heading y del Centrado (str_lateral). Si la necesidad de corregir la posición lateral (str_lateral) para no chocar con la pared es más drástica que la de mantener la orientación actual (str_heading), el control de centrado toma prioridad absoluta y devuelve str_lateral. De lo contrario, el robot ignora el centrado fino y sigue su rumbo normal. 

<img width="592" height="49" alt="Pilar 34" src="https://github.com/user-attachments/assets/56af8f80-32e3-40b0-a7d2-59ddc7482e3f" />

**Velocidad Adaptativa:** Estipulamos 2 velocidades distintas para las curvas y para las rectas, permitiendo la mayor estabilidad. Las velocidades establecidas en 0.25 m/s y 0.4 m/s son el 50% de las velocidades iniciales que establecimos y que están por debajo de la velocidad teórica que habíamos calculado. Sin embargo, está velocidades en la práctica nos permitió tener mayor nivel de confiabilidad y evitar choques por retraso en alguna detección. 

<img width="591" height="105" alt="Pilar35" src="https://github.com/user-attachments/assets/0dbd60b7-cef4-4b1d-9d6f-b832c7e2c628" />

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

## 6e. Diagrama de Flujo de Reto Abierto

<img width="1911" height="1077" alt="Reto1" src="https://github.com/user-attachments/assets/8688b286-6c20-4c30-901a-c8fbc9baaf0d" />




## 6f. Métricas de Desempeño del Reto Abierto 

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

**Solución:** Reimprimir el engranaje en resina de Nylon, mucho mas resistente al calor y a la fricción que el PLA que utilizamos en el engranaje anterior. Una vez solucionados en las prácticas volvimos a obtener tiempos entre 42 y 38 segundos. 

<img width="722" height="400" alt="Resultados Regional 1 2026" src="https://github.com/user-attachments/assets/dfc9c8f8-c718-4969-aeb3-4f4e9d9558e1" />


## 6g. Ajustes Realizados 

- Inicialmente diseñamos una detección de sentido pre-arranque más ambiciosa analizando discontinuidades del LiDAR mientras el robot estaba estacionario. La idea era detectar el lado en donde estaban las discontinuidades más importantes, para detectar hacia qué lado estaba la apertura, pero la tasa de éxito dependía mucho de la posición inicial del robot por lo que pasamos a una estrategia más reactiva como la comentada en el _Pilar 2_ . 

- Al comienzo habíamos establecido, que una vez que el robot comenzara a girar, saliera del modo giro cuando el error con respecto al ángulo objetivo ya se hubiera reducido a 45° (la mitad), esto para evitar sobregiros por la velocidad pasando el P Controller de un KP_GIRO más alto a  KP_RECT mas gradual, pero obtuvimos muchos subgiros y activación de aperturas no reales que provocaban nuevos giros. La solución: 

   - Luego de un proceso iterativo redujimos el error para pasar de KP_GIRO a KP_RECT de 45° a 15° 

   - Redujimos las velocidades a la mitad, quedando en 0.4 m/s en rectas y 0.25 m/s en curvas. Favoreciendo confiabilidad vs velocidad. 

Con estos ajustes logramos una tasa de éxito muy elevada incluso con cambios en el tamaño del cuadro central a 1,4m y 1,8 m por lado. La velocidad reducida y el esquema dual del P-Controller han permitido que los ajustes post giro se han muy leves y a veces imperceptibles. 

## 7. Pensamiento Sistémico y Decisiones de Ingeniería (Criterio 4)

Esta sección documenta cómo los subsistemas del robot trabajan juntos, las restricciones que dieron forma al diseño, las decisiones principales con sus alternativas, y el historial de iteraciones. El análisis técnico extendido (con cálculos, código y diagnósticos está en el **Engineering Journal, sección 7**.

## 7a. Diagrama de Bloques del Sistema

<img width="1104" height="602" alt="Diagrama de Subsistemas" src="https://github.com/user-attachments/assets/495105a4-db5d-4ad6-80fe-070cfcc5d145" />

## 7b. Interacción entre Subsistemas

| Subsistema A | Subsistema B | Interacción |
|---|---|---|
| LiDAR STL-27L | Control (RPi 5) | Publica `/scan` a 10 Hz → control extrae sectores frontal/laterales |
| Cámara GS + lente 2.8 mm | Nodo de visión (RPi 5) | Detecta pilares R/G/M y publica `/pilares` (formato `R:cx:h;G:cx:h`) |
| Pico Plus 2 | RPi 5 | UART USB 921600 baud, CSV → topics `/npcpos`, `/imu`, `/encoder`, `/start` |
| IMU BNO085 | Pico Plus 2 | I²C 100 Hz → integración con encoder produce `POS,x,y,θ,acc_yaw` |
| Encoder motor | Pico Plus 2 | Interrupción RISING en GP2 + lectura GP3 → odometría a 100 Hz |
| Control (RPi 5) | Pico Plus 2 | Publica `/cmd_motor` (m/s) y `/cmd_servo` (-1..+1) a 40 Hz |
| Pico Plus 2 | VNH5019 | INA/INB + PWM 20 kHz (GP8/9/12) → tracción |
| Pico Plus 2 | Servo Savox | PWM 50 Hz en GP15 → dirección Ackermann |
| ToF VL53L4CD ×2 | Pico Plus 2 | I²C vía Qwiic MultiPort, reservados para parking Reto 2 |
| Botón físico (GP28) | Pico Plus 2 → RPi 5 | Publica `/start` → control captura `section_angle` al arrancar |

## 7c. Restricciones (Constraints) Identificadas

| Restricción | Límite | Impacto en el diseño |
|---|---|---|
| Dimensiones máximas | 300 × 200 × 300 mm (regla WRO 2026) | Llevó a chasis personalizado 230×150×126 mm |
| Peso máximo | 1500 g | El robot final pesa 1100 g (margen +400 g) |
| Altura paredes pista | 10 cm | **Forzó LiDAR al primer piso adelantado** para barrer a la altura correcta |
| Altura pilares (Reto 2) | ~10 cm coloreados R/G | **Forzó lente CCTV 2.8 mm (FoV 96°)** para capturar pilares cercanos |
| FoV útil del LiDAR | Solo 193°–350° (157° hacia adelante) | **Todos los sectores del control deben estar dentro de ese rango** |
| Voltaje mínimo bus motor | 12 V nominal | **Forzó LiPo 3S** (2S no era suficiente) |
| Pico de corriente servo | hasta 3.5 A | **Forzó regulador 5V dedicado** al servo (D36V50F5) |
| Sin Wi-Fi en la pista | 0 conectividad | Arranque autónomo vía systemd + botón físico |
| Tiempo de boot | ~40 s | Aceptado: priorizamos estabilidad sobre velocidad |
| Latencia control 40 Hz | <25 ms por ciclo | Determinó protocolo CSV simple sobre micro-ROS |

## 7d. Decisiones de Diseño Principales

Esta subsección resume las decisiones de ingeniería más importantes con su razonamiento. 
**Cada decisión sigue el patrón "elegimos X en vez de Y porque…"** 

### Decisión 1 — Arquitectura: RPi 5 como Cerebro + Pico 2 como ejecutor y reportador de datos 

| Opciones consideradas | Veredicto |
|---|---|
| **A: Toda la lógica en RPi 5, Pico solo sensores y actuadores** | ✓ **Elegida** |
| B: Lógica distribuida (RPi 5 alto nivel, Pico control local) | Descartada |
| C: Todo en Pico, sin Pi 5 | Descartada |

**Por qué A:** Python en la Pi 5 acelera la iteración de algoritmos
(ROS 2, OpenCV); el Pico ofrece tiempo real estricto para encoder e
IMU; la frontera entre los dos es un protocolo CSV legible. **El
Pico es deliberadamente ejecutor:** no decide, solo ejecuta.

### Decisión 2 — Lógica del Open Challenge: 4 pilares en lugar de máquina de estados compleja

| Pilares | Función |
|---|---|
| **Pilar 1** | Localización (odometría) y conteo de **12 giros** (interpretación más robusta) |
| **Pilar 2** | Detección de esquinas (mediana frontal + confirmación lateral + debounce espacial) |
| **Pilar 3** | Control en 3 capas (heading, wall-centering, velocidad adaptativa) |
| **Pilar 4** | Fin de carrera con banda de parada 1,2 a 1,5m |

**Por qué 4 pilares y no máquina de estados grande:** la máquina se reduce a solo 5 estados (`BOOT → READY → RUNNING → FINISH_APPROACH → STOPPED`); el resto de la complejidad vive como capas dentro del estado `RUNNING`, fácil de tunear capa porcapa sin tocar las otras.

### Decisión 3 — Reto 2: Siguiendo Camino de 3 capas

| Capa | Función | Sensor principal |
|---|---|---|
| **Capa 1 — Ruta Proyectada** | Ray marching para encontrar la mejor dirección libre | LiDAR |
| **Capa 2 — Recorte por color** | Rutas posibles se limitan según color del pilar (rojo→derecha, verde→izquierda) | Cámara |
| **Capa 3 — SpiderSense** | Reflejo lateral de emergencia si un pilar o pared se acerca demasiado | LiDAR |

**Por qué navegación reactiva y no detección de eventos:** la busqueda de ruta más profunda maneja curvas y pilares implícitamente, sin la necesidad de "detección
de esquina, que es mas dificil en la presencia de obstaculos. La cámara es solo semáforo de color (rojo/verde), no estima distancia. La distancia la lleva el LiDAR.

### Decisión 4 — Conteo de vueltas por yaw acumulado, no por esquinas

**Por qué |acc_yaw| > 900° en Reto 2** (en lugar de contar giros como en Reto 1): los pilares fuerzan trayectorias no rectangulares; el robot puede "girar" 90° por una curva *o* por una evasión, y
contar esquinas confundiría ambas. El yaw acumulado es robusto en ambos casos.

### Decisión 5 — Detección de sentido CW/CCW en la primera esquina

**Antes:** intentábamos detectar sentido con discontinuidades del LiDAR antes de arrancar (robot quieto).
**Problema:** en pruebas no funcionaba consistentemente.
**Decisión:** adoptar enfoque de esperar a la primera esquina y elegir el lado con apertura.
**Resultado:** robusto, se eliminó un estado `DETECTING_SENSE` que estaba presente en una versión inicial del Reto 1.

## 7.5 Análisis de Riesgos y Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación implementada |
|---|---|---|---|
| Caída del riel 5V por pico del servo | Media | Reset de la RPi 5 a mitad de carrera | **Regulador dedicado al servo** (D36V50F5) |
| EMI del motor sobre IMU | Media | Yaw inestable | IMU en piso superior + canales de cable separados |
| LiDAR no ve paredes de 10 cm | Alta si mal montado | Imposibilidad de centrarse | **LiDAR en primer piso, no en piso superior** |
| ToF lee basura a <15 mm | Alta | Lecturas espurias en parking | Sensor retraído ≥15 mm + filtro software |
| Cámara con rolling shutter distorsiona | Alta | Falsos positivos de pilar | **Global shutter elegida específicamente** |
| Variación de iluminación en pista | Alta | Falla detección de color | Calibración HSV in-situ con `calibrador_hsv.py` |
| Pérdida de comunicación Pi ↔ Pico | Baja | Robot fuera de control | Reconexión USB automática en bridge + watchdog firmware (pendiente) |
| Robot atascado contra pared | Media | Pérdida de la ronda | SpiderSense reflejo lateral (Capa 3 Reto 2) |


## 7.6 Historial de Iteraciones (resumen)

| Versión | Cambio principal | Resultado |
|---|---|---|
| **V1.0** | Diseño inicial 3 pisos, motor 20.4:1, batería 2S, servo PS1171MG, LiDAR arriba | Demasiado alto, par insuficiente, LiDAR no ve paredes bajas |
| **V2.0** | Rediseño chasis 2 pisos + subnivel, motor 34:1, batería 3S, servo Savox SC-1251MG, LiDAR abajo y adelante | Geometría compacta, Ackermann real, LiDAR ve paredes |
| **V3.0** | Servo movido detrás de las ruedas delanteras, doble regulador 5V, canales de cable modulares | Sistema robusto, aislamiento de transitorios, cableado limpio |
| **Open Challenge V1** | 4 pilares con detección de sentido pre-arranque | No funcionaba consistentemente |
| **Open Challenge V2** | Detección de sentido en primera esquina, UMBRAL_FIN_GIRO bajado a 15° | Estable en 2+ días de pruebas en pista oficial |
| **Reto 2 V1** | Gap follower de 3 capas "Siguiendo Camino" | En depuración (varios bugs encontrados y corregidos, ver Journal) |

# 8. Instrucciones de Reproducibilidad

> *Criterio 5 — Rúbrica WRO Future Engineers 2026.*
> Esta sección permite que **otro equipo pueda replicar el robot
> NPC desde cero**. Incluye lista de hardware con links de compra,
> requisitos de software, instalación paso a paso, estructura del
> repositorio, archivos CAD/3D y procedimiento de arranque en
> competencia.

## 8.1 Requisitos de Hardware

Lista completa de componentes utilizados, con sus links de compra
oficiales. La lista detallada con descripción y precios está en
[`/docs/lista-componentes.md`](./lista-componentes.md).

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
| | Eje trasero | KYX Racing Steel Drive Shaft (Tamiya DT04) | 1 | KYX Racing |
| | Manguetas Ackermann | KYX Racing Aluminum Steering Knuckles | 2 | KYX Racing |
| | Servo saver | Tamiya TT-02 Hi-Torque + horn aluminio | 1 | Tamiya |
| | Tie rods | M3 ajustables uxcell | 2 | uxcell |
| | Ejes | Acero inoxidable 5 mm × 100 mm uxcell | 2 | uxcell |
| **Cables** | USB-C Pi↔Pico | SUNGUY USB-C 3.1 Gen2 — 6 in y 1 ft | 2 | Amazon |
| **Mecánica 3D** | Filamento | PLA Bambu Lab | — | Bambu Lab |
| | Impresora 3D | Bambu Lab P2S | — | Bambu Lab |

## 8.2 Requisitos de Software

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
- Arduino IDE 2.3.8
- Board package: Earle Philhower RP2350 (para Pico Plus 2)
- Librerías Arduino: Adafruit BNO08x, SparkFun VL53L4CD
- Autodesk Fusion 360 (CAD)
- Bambu Studio (laminado e impresión)
- Git
```

## 8.3 Instalación Paso a Paso

### 1) Preparar la Raspberry Pi 5

```bash
# Sistema operativo Ubuntu 24.04
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-opencv python3-numpy python3-pip

# ROS 2 Jazzy (siguiendo guía oficial)
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

```bash
ros2 run npc_bot calibrador_hsv
```

> Interfaz interactiva con sliders para rangos HSV de rojo, verde y
> magenta. Calibrar **bajo iluminación de la pista oficial**, no en
> laboratorio.

### 7) Servicio systemd (auto-arranque, requerido por reglas WRO 9.6–9.14)

```bash
sudo cp src/systemd/npc_bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable npc_bot.service
sudo systemctl start npc_bot.service
```

> Tiempo de boot hasta robot listo: **~40 segundos** desde encendido
> al pitido de "READY".

## 8.4 Estructura del Repositorio

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

## 8.5 Cómo Arrancar el Sistema (procedimiento de carrera)

### Opción A — Arranque automático (recomendado en competencia)

```
1. Conectar batería LiPo 3S
2. Encender interruptor principal
3. Esperar ~40 s (LED indicador en verde fijo = listo)
4. Colocar robot en la pista en posición de salida
5. Presionar botón físico (GP28) → el robot captura section_angle
   y arranca la lógica de carrera
```

### Opción B — Arranque manual (para depuración)

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

## 8.6 Archivos CAD / 3D

Todos los archivos están en [`/models`](../models/) en formato STL
(geometría) y 3MF (proyecto Bambu Studio con parámetros de impresión).

| Pieza | Archivo | Material | Tiempo de impresión |
|---|---|---|---|
| Chasis Abajo V2 (primer piso) | `Chassis Abajo V2.stl` / `.3mf` | PLA | 12 h |
| Chasis Arriba V2 (2do piso + subnivel) | `Chassis Arriba V2.stl` / `.3mf` | PLA | Pendiente |
| Gear Box Diferencial | `Gear Box Diferencial.stl` / `.3mf` | PLA | Pendiente |
| Gear Diferencial (engranajes cónicos) | `Gear Diferencial.stl` / `.3mf` | PLA | Pendiente |
| Gear Motor con Flange | `Gear Motor con Flange.stl` / `.3mf` | PLA | Pendiente |
| Soporte Motor VF | `Soporte Motor VF.stl` / `.3mf` | PLA | Pendiente |
| Soporte Servo VF | `Soporte Servo VF.stl` / `.3mf` | PLA | Pendiente |
| Repisa | `Repisa.stl` / `.3mf` | PLA | Pendiente |
| Espaciador de Eje | `Espaciador de Eje.stl` / `.3mf` | PLA | Pendiente |
| Canal Cables 2 / 3 / 4 + Tapas | `Canal 2/3/4 Cables [Tapa].stl` | PLA | Pendiente |
| Sujetador Cables | `Sujetador Cables.stl` / `.3mf` | PLA | Pendiente |
| Motor Pololu 25D (referencia) | `25d-metal-gearmotor-34-47-encoder.step` | — | (modelo importado del fabricante) |

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

## 8.7 Notas de Ensamblaje

> **Pendiente de redactar:** secuencia de ensamblaje paso a paso.
> Sugerencia: incluir 6–8 fotos del proceso (primer piso completo,
> diferencial montado, eje trasero, servo + dirección, segundo piso,
> ensamble final).

Resumen del orden recomendado:

1. Imprimir todas las piezas
2. Ensamblar diferencial: insertar engranajes cónicos en `Gear Box Diferencial`
3. Montar eje trasero KYX con diferencial en el `Chassis Abajo V2`
4. Montar motor Pololu 34:1 con `Soporte Motor VF` y `Gear Motor con Flange`
5. Montar servo Savox **detrás de las ruedas delanteras** (`Soporte Servo VF`)
6. Conectar manguetas KYX + tie rods M3 + servo saver Tamiya
7. **Ajustar convergencia (toe-in ≈ 0.5 mm)** con servo centrado
8. Montar VNH5019, reguladores y batería en el primer piso
9. Montar Raspberry Pi 5, Pico Plus 2 y sensores en el segundo piso
10. Ruteo de cables por los canales modulares (`Canal 2/3/4`)
11. Calibrar IMU (figura de 8) y encoder (`2006 ticks/m` validados)
12. Calibrar HSV de la cámara bajo iluminación de la pista

---
