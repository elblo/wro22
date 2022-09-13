from picar import front_wheels, back_wheels
import picar

import time
import RPi.GPIO as GPIO

# Configuración inicial del coche
picar.setup()

bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()

motor_speed = 60
bw.speed = 0 
fw.offset = 0
fw.turn(90)

# Constantes con los pines GPIO utilizados
# TODO Poner números de pines correctamente
ULTRASOUND_LEFT_TRIG = 16
ULTRASOUND_LEFT_ECHO = 20

ULTRASOUND_RIGHT_TRIG = 16
ULTRASOUND_RIGHT_ECHO = 20

ULTRASOUND_FRONT_TRIG = 16
ULTRASOUND_FRONT_ECHO = 20

BUTTON = 5

# Configuración de los modos GPIO, botones...
def setup():
    # Modo del GPIO. Alternativa: GPIO.BOARD
    GPIO.setmode(GPIO.BCM)  

    # Configuración pines sensor ultrasonidos izquierdo
    GPIO.setup(ULTRASOUND_LEFT_TRIG, GPIO.OUT)
    GPIO.setup(ULTRASOUND_LEFT_ECHO, GPIO.IN)

    # TODO Añadir la configuración de pines para los otros 2 sensores de ultrasonidos

    # Configuración pin botón como entrada habilitando una resistencia de pull_up interna, 
    # para prescindir así de la resistencia física en el circuito
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

# Devuelve distancia a sensor ultrasonidos en cm
# Parámetros de entrada: Pines trigger y echo
def distance(trig, echo):
    GPIO.output(trig, 0)
    time.sleep(0.000002)

    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

    while GPIO.input(echo) == 0:
        a = 0
    startTime = time.time()

    while GPIO.input(echo) == 1:
        a = 1
    stopTime = time.time()

    timeElapsed = stopTime - startTime

    # El tiempo que tarda la onda entre que se se emite y se recibe
    # se multiplica por la velocidad del sonido (343 m/s) pasada a cm (34.300 cm/s)
    # y se divide entre 2 (ida y vuelta de la onda)
    return timeElapsed * 34300 / 2

# Función con el código principal a ejecutar 
def loop():
    # Inicio cuando se pulsa el botón
    while True:
        if GPIO.input(BUTTON) == GPIO.LOW:

            while True:
                disLeft = distance(ULTRASOUND_LEFT_TRIG, ULTRASOUND_LEFT_ECHO)
                print ('Distancia izquierda: ', disLeft, ' cm')
                print ('')

                # TODO Declarar variables disRight y disFront asignándole lo que devuelva
                # la función distance llamándola con las constantes de los pines correspondientes

                # Adelante
                bw.speed = motor_speed
                bw.backward()
                print("Adelante: ", bw.speed)

                time.sleep(1)

# Función con el código a ejecutar antes de salir del script
def destroy():
    # Limpiar los puetos usados del GPIO
    GPIO.cleanup()
    # Parar coche
    bw.stop()

# Programa principal
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()