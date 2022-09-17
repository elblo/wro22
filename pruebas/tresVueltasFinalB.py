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

# Variables para giros
anguloRecto = 87
anguloGiroIzq = 45
anguloGiroDcha = 135
distanciaGiro = 180

# Constantes con los pines GPIO utilizados
ULTRASOUND_LEFT_TRIG = 19
ULTRASOUND_LEFT_ECHO = 26

ULTRASOUND_RIGHT_TRIG = 5
ULTRASOUND_RIGHT_ECHO = 6

#ULTRASOUND_FRONT_TRIG = 16
#ULTRASOUND_FRONT_ECHO = 20

BUTTON = 13

# Configuración de los modos GPIO, botones...
def setup():
    # Modo del GPIO. Alternativa: GPIO.BOARD
    GPIO.setmode(GPIO.BCM)  

    # Configuración pines sensor ultrasonidos izquierdo
    GPIO.setup(ULTRASOUND_LEFT_TRIG, GPIO.OUT)
    GPIO.setup(ULTRASOUND_LEFT_ECHO, GPIO.IN)

    # TODO Añadir la configuración de pines para los otros 2 sensores de ultrasonidos
    # Configuración pines sensor ultrasonidos derecha
    GPIO.setup(ULTRASOUND_RIGHT_TRIG, GPIO.OUT)
    GPIO.setup(ULTRASOUND_RIGHT_ECHO, GPIO.IN)
    
    # Configuración pines sensor ultrasonidos delantero
    #GPIO.setup(ULTRASOUND_FRONT_TRIG, GPIO.OUT)
    #GPIO.setup(ULTRASOUND_FRONT_ECHO, GPIO.IN)
    
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

# Giro derecha 
def giroDcha():
    print("Gira a derecha")
    # Inicia giro derecha
    for x in range(2):
        fw.turn(anguloGiroDcha)
        # Adelante
        #bw.speed = motor_speed 
        #bw.backward() 
        time.sleep(0.5) 
    # Movimiento recto para cuadrarse durante 4 * 0,5 = 2 segundos
#     for x in range(3):
#         fw.turn(anguloRecto)
#         # Adelante
#         #bw.speed = motor_speed
#         #bw.backward()
#         time.sleep(0.6) 

# Giro izquierda
def giroIzq():
    print("Gira a izquierda")
    # Inicia giro a izquierda
    for x in range(3):
        fw.turn(anguloGiroIzq)
        # Adelante
        #bw.speed = motor_speed
        #bw.backward()
        time.sleep(0.4) 
    # Movimiento recto para cuadrarse durante 4 * 0,5 = 2 segundos
#     for x in range(3):
#         fw.turn(anguloRecto)
#         # Adelante
#         #bw.speed = motor_speed
#         #bw.backward()
#         time.sleep(0.6) 

# Movimiento recto corrigiendo dirección
def recto(disDer, disIzq):
    # Corregir posición --> sensor derecha menos izquierda dividido entre 2 (factor de corrección)
    # Si sale positivo --> derecha
    # Si sale negativo --> izquierda
    correccionPosicion = (disDer - disIzq) / 2
    if correccionPosicion > 20:
        correccionPosicion = 20
    if correccionPosicion < -20:
        correccionPosicion = -20
    print("Distancia derecha menos izquierda: %.1f cm" % correccionPosicion)
    # Giro corregido
    fw.turn(anguloRecto + correccionPosicion)

# Movimiento recto con referencia exterior IZQUIERDA
def rectoSensorIzq(disLeftPrevious, disLeftNow):
    # Corregir posición --> sensor izquierdo
    correccionPosicion = (disLeftPrevious - disLeftNow) * 2
    print("Corrección izquierda: %.1f cm" % correccionPosicion)
    # Giro corregido
    fw.turn(anguloRecto + correccionPosicion)

# Movimiento recto con referencia exterior DERECHA
def rectoSensorDcha(disRightPrevious, disRightNow):
    # Corregir posición --> sensor derecho
    correccionPosicion = (disRightNow - disRightPrevious) * 2
    print("Corrección derecha: %.1f cm" % correccionPosicion)
    # Giro corregido
    fw.turn(anguloRecto + correccionPosicion)
    
# Función con el código principal a ejecutar 
def loop():
    # Inicio cuando se pulsa el botón
    while True:
        if GPIO.input(BUTTON) == GPIO.LOW:
            
            disLeftPrevious = distance(ULTRASOUND_LEFT_TRIG, ULTRASOUND_LEFT_ECHO)
            disRightPrevious = distance(ULTRASOUND_RIGHT_TRIG, ULTRASOUND_RIGHT_ECHO)
            print ('Distancia izquierda PREVIA: ', disLeftPrevious, ' cm')

            # Ponemos el coche recto para empezar
            fw.turn(anguloRecto)
            # Adelante
            bw.speed = motor_speed
            bw.backward()
            
            direccion = ""

            decimasRecto = -1
            # 3 vueltas = 12 giros
            giros = 0
            while giros < 12:
                # Medimos distancia a izquierda y derecha cada 0.2 segundos (sleep al final del while)
                disLeftNow = distance(ULTRASOUND_LEFT_TRIG, ULTRASOUND_LEFT_ECHO)    
                disRightNow = distance(ULTRASOUND_RIGHT_TRIG, ULTRASOUND_RIGHT_ECHO)
                print ("Distance LEFT <-- %.1f cm COCHE --> %.1f cm RIGHT" %(disLeftNow, disRightNow))

                # Determinar la dirección (primer giro)
                if direccion == "":
                    if disLeftNow > distanciaGiro:
                        direccion = "izquierda"
                        print("Dirección IZQUIERDA")
                    if disRightNow > distanciaGiro:
                        direccion = "derecha"
                        print("Dirección DERECHA")

                # Giro a izquierda 
                if (disLeftNow > distanciaGiro) and (direccion == "izquierda") and (decimasRecto < 0):
                    giroIzq()                
                    giros = giros + 1
                    decimasRecto = 18
            
                # Giro a derecha
                elif (disRightNow > distanciaGiro) and (direccion == "derecha") and (decimasRecto < 0):
                    giroDcha()
                    giros = giros + 1
                    decimasRecto = 18
                      
                # Coche va recto
                else:                
                    #recto(disRightNow, disLeftNow)
                    if direccion == "izquierda" or direccion == "":
                        rectoSensorDcha(disRightPrevious, disRightNow)
                    if direccion == "derecha":
                        rectoSensorIzq(disLeftPrevious, disLeftNow)
                        
                ###
                decimasRecto = decimasRecto - 1
                print("Giros: " + str(giros))
                disLeftPrevious = disLeftNow
                disRightPrevious = disRightNow
                time.sleep(0.1)
            
            # Al finalizar los 12 giros (3 vueltas) paramos a la espera de pulsar el botón de nuevo para empezar
            fw.turn(anguloRecto)
            time.sleep(1.0)
            bw.stop()


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
        