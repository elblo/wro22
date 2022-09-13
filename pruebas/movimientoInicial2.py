from picar import front_wheels, back_wheels

import picar
from time import sleep

picar.setup()


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