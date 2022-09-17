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
ULTRASOUND_LEFT_TRIG = 19
ULTRASOUND_LEFT_ECHO = 26

ULTRASOUND_RIGHT_TRIG = 5
ULTRASOUND_RIGHT_ECHO = 6

ULTRASOUND_FRONT_TRIG = 16
ULTRASOUND_FRONT_ECHO = 20

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

# Función con el código principal a ejecutar 
def loop():
    # Inicio cuando se pulsa el botón
    while True:
        if GPIO.input(BUTTON) == GPIO.LOW:
            
            disLeftPrevious = distance(ULTRASOUND_LEFT_TRIG, ULTRASOUND_LEFT_ECHO)
            print ('Distancia izquierda PREVIA: ', disLeftPrevious, ' cm')
            
            # Corrección de la trayectoria
            anguloRecto = 85
            fw.turn(anguloRecto)

            # Variables
            distanciaGiro = 200
            anguloGiroIzq = 45
            anguloGiroDcha = 135
            
            # 3 vueltas = 12 giros
            giros = 0
            while giros < 12:
                
                # Adelante
                bw.speed = motor_speed
                bw.backward()
                
                disLeftNow = distance(ULTRASOUND_LEFT_TRIG, ULTRASOUND_LEFT_ECHO)    
                disRightNow = distance(ULTRASOUND_RIGHT_TRIG, ULTRASOUND_RIGHT_ECHO)
                print ("Distance LEFT <-- %.1f cm COCHE --> %.1f cm RIGHT" %(disLeftNow, disRightNow))

                # Giro a izquierda 
                if disLeftNow > distanciaGiro :
                    print("Gira a la izquierda")
                    # Inicia giro a izquierda
                    for x in range(2):
                        
                        # Giro derecha
                        fw.turn(anguloGiroIzq)
                        # Adelante
                        bw.speed = motor_speed
                        bw.backward()
                        
                        time.sleep(0.5) # También puede interesar ajustar este tiempo

                    
                    # Movimiento durante 4 * 0,5 = 2 segundos
                    for x in range(3):
                
                
                        fw.turn(anguloRecto)
                        # Adelante
                        bw.speed = motor_speed
                        bw.backward()
                        # Giro izquierda
                        #fw.turn(anguloGiroIzq)
  
                        time.sleep(0.6) # También puede interesar ajustar este tiempo
                
                    giros = giros + 1 
            
                # Giro a derecha
                elif disRightNow > distanciaGiro:
                    print("Gira a la derecha")
                    # Inicia giro derecha
                    for x in range(2):
                        
                        # Giro derecha
                        fw.turn(anguloGiroDcha)
                        # Adelante
                        bw.speed = motor_speed
                        bw.backward()
                        
                        time.sleep(0.5) # También puede interesar ajustar este tiempo

                    
                    # Movimiento durante 4 * 0,5 = 2 segundos
                    for x in range(3):
                
                
                        fw.turn(anguloRecto)
                        # Adelante
                        bw.speed = motor_speed
                        bw.backward()
                        # Giro izquierda
                        #fw.turn(anguloGiroIzq)
  
                        time.sleep(0.6) # También puede interesar ajustar este tiempo
                
                    # TODO Llamada a función giro derecha en vez de la instrucción para girar de arriba
                    giros = giros + 1
                      
                # Coche va recto
                else:
                
                    # Adelante
                    #bw.speed = motor_speed
                    #bw.backward()
                
                    # Corregir posición --> sensor derecha menos izquierda dividido entre 2 (factor de corrección)
                    # Si sale positivo --> derecha
                    # Si sale negativo --> izquierda
                    correccionPosicion = (disRightNow - disLeftNow) / 2
                    if correccionPosicion > 20:
                        correccionPosicion = 20
                    if correccionPosicion < -20:
                        correccionPosicion = -20
                    #print("Distancia derecha menos izquierda: %.1f cm" %(correccionPosicion))
                    
                    # Giro corregido
                    fw.turn(anguloRecto+correccionPosicion)
                           
                    disLeftPrevious = disLeftNow
                    #time.sleep(0.2) # También puede interesar ajustar este tiempo
                        
                        
                print(giros)
                disLeftPrevious = disLeftNow
                time.sleep(0.2)
            
            bw.stop()

                
# Giro derecha 
def girodcha():
    anguloGiroDcha = 135
    fw.turn (anguloGiroDcha)
    time.sleep(1.8) # Determinar el tiempo necesario para hacer el giro completo

# TODO Funcióin Giro izquierda

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
        