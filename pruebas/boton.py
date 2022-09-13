from picar import front_wheels, back_wheels

import picar
from time import sleep

picar.setup()

import RPi.GPIO as GPIO #Importamos el paquete RPi.GPIO y en el código nos refiriremos a el como GPIO
import time #Importamos el paquete time


pin_btn = 5 #Variable que contiene el pin(GPIO.BCM) al cual conectamos la señal del botón

GPIO.setmode( GPIO.BCM )        #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi
GPIO.setup( pin_btn , GPIO.IN , pull_up_down=GPIO.PUD_UP ) #Configuramos el pin del botón como Entrada y habilitamos una resistencia de pull_up interna, por lo que podríamos presindir de la resistencia de pull_up física ennuestro circuito



#Contenemos el código principal en un aestructura try para limpiar los GPIO al terminar o presentarse un error
try:
    while 1: #Implementamos un loop infinito
        if GPIO.input( pin_btn ) == GPIO.LOW:   #Si la lectura al pin del botón resulta 0/GPIO.LOW ejecutamos el código del if
            print("Boton presionado")           #Hacemos una impresión en consola 
            time.sleep(0.3)                     #Nos mantenemos en esta línea por 0.3 segundos para dar tiempo a que el botón se libere y el estado del led no cambie varias veces en un solo botonazo  

except KeyboardInterrupt:
    # CTRL+C
    print("\nInterrupcion por teclado")
except:
    print("Otra interrupcion")
finally:
    GPIO.cleanup()
    print("GPIO.cleanup() ejecutado")