# wro22
Repositorio con el código y documentación sobre la participación del equipo AWIWI FERNANDO III en la WRO Future Engineers 2022

## Hardware utilizado
1. Raspberry Pi 3 Model B
2. Kit Sunfounder Picar-V
3. Sensores ultrasonidos HC-SR04
4. Cámara Raspberry Pi V2 8MP
5. Pulsador, cables, protoboard...

## Software
1. Raspberry OS 
2. Python 3
3. Librerías específicas para conexión con GPIO de la Raspberry y pines de la placa Robo Hat [link](https://github.com/sunfounder/SunFounder_PiCar-V)
4. Librería OpenCV para visión artificial [link](https://opencv.org/)
5. VNC para conexión remota a la Raspberry [link](https://www.realvnc.com/es/connect/download/viewer/)

## Conexión a Raspberry mediante VNC
Descargar en ordenador el cliente de VNC y conectar al servidor VNC instalado en la Raspberry. Desde el PC hay que indicar la IP de la raspberry y el usuario y contraseña, por defecto: pi | raspberry.

## Directorios de librerías
Descargar en */home/pi* el repositorio de GitHub [Picar-V](https://github.com/sunfounder/SunFounder_PiCar-V). Ejecutar el script **install_dependencies** para que realice la descarga e instalación de las librerías necesarias en */home/pi/SunFounder_Picar/*.

## Directorio de trabajo
En */home/pi/wro22/* se localizan todos los documentos y scripts desarrollados, tanto de prueba como para la versión final de la tarea.

## Ejecución automática del script
Para ejecutar de forma automática el script **tresVueltasFinalB.py** en segundo plano una vez cargue el sistema operativo, hay que añadir la siguiente línea al fichero */etc/rc.local* antes de la línea *exit 0*:
`python3 /home/pi/wro22/pruebas/tresVueltasFinalB.py &`





