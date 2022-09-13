from picar import front_wheels, back_wheels

import picar
from time import sleep

picar.setup()

import RPi.GPIO as GPIO #Importamos el paquete RPi.GPIO y en el código nos refiriremos a el como GPIO
import time #Importamos el paquete time


pin_btn = 5 #Variable que contiene el pin(GPIO.BCM) al cual conectamos la señal del botón

GPIO.setmode( GPIO.BCM )        #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi
GPIO.setup( pin_btn , GPIO.IN , pull_up_down=GPIO.PUD_UP ) #Configuramos el pin del botón como Entrada y habilitamos una resistencia de pull_up interna, por lo que podríamos presindir de la resistencia de pull_up física ennuestro circuito



rear_wheels_enable  = True
front_wheels_enable = True


bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()




fw.offset = 0


bw.speed = 0


motor_speed = 60
def nothing(x):
    pass

def main():
    fw_angle = 90
    
    print("Begin!")

     
    
    print("Inicio")


    while 1: #Implementamos un loop infinito
        if GPIO.input( pin_btn ) == GPIO.LOW:   #Si la lectura al pin del botón resulta 0/GPIO.LOW ejecutamos el código del if
            print("Boton presionado")           #Hacemos una impresión en consola 


            if rear_wheels_enable:
            #         fw.turn(120)
                # Adelante
                fw.turn(85)
                bw.speed = motor_speed
            #         movimiento hacia delante
                for x in range(500):
                    bw.backward()
                    
            #             angulo = angulo + 1
            #             fw.turn(angulo)

                    sleep(0.01)
                    print("hacia delante el coche")
                    
                fw.turn(45)
            #         giro izquierda
                for x in range (130):
                    bw.backward()
                    sleep(0.01)
                    print("giro")
                # Adelante
                fw.turn(85)
                bw.speed = motor_speed
            #         movimiento hacia delante
                for x in range(500):
                    bw.backward()
                    
            #             angulo = angulo + 1
            #             fw.turn(angulo)

                    sleep(0.01)
                    print("hacia delante el coche")
                    
                fw.turn(45)
            #         giro izquierda
                for x in range (130):
                    bw.backward()
                    sleep(0.01)
                    print("giro")


                # Adelante
                fw.turn(85)
                bw.speed = motor_speed
            #         movimiento hacia delante
                for x in range(500):
                    bw.backward()
                    
            #             angulo = angulo + 1
            #             fw.turn(angulo)

                    sleep(0.01)
                    print("hacia delante el coche")
                    
                fw.turn(45)
            #         giro izquierda
                for x in range (130):
                    bw.backward()
                    sleep(0.01)
                    print("giro")
                # Adelante
                fw.turn(85)
                bw.speed = motor_speed
            #         movimiento hacia delante
                for x in range(500):
                    bw.backward()
                    
            #             angulo = angulo + 1
            #             fw.turn(angulo)

                    sleep(0.01)
                    print("hacia delante el coche")
                    
                fw.turn(45)
            #         giro izquierda
                for x in range (130):
                    bw.backward()
                    sleep(0.01)
                    print("giro")
                # Adelante
                fw.turn(85)
                bw.speed = motor_speed
            #         movimiento hacia delante
                for x in range(500):
                    bw.backward()
                    
            #             angulo = angulo + 1
            #             fw.turn(angulo)

                    sleep(0.01)
                    print("hacia delante el coche")
                    
                fw.turn(45)
            #         giro izquierda
                for x in range (130):
                    bw.backward()
                    sleep(0.01)
                    print("giro")

            bw.stop()
def test():
    fw.turn(90)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()