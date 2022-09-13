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
fw.turn(90)


motor_speed = 60

def nothing(x):
    pass

def main():
    fw_angle = 90
    
    print("Begin!")
    while True:

        if rear_wheels_enable:
            # Adelante
            for x in range(100):
                bw.speed = motor_speed
                bw.backward()
                sleep(0.01)
                print("se mueve el coche")
            
                
            
        else:
            bw.stop()


def destroy():
    bw.stop()

def test():
    fw.turn(90)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()