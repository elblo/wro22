from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep


picar.setup()
# Show image captured by camera, True to turn on, you will need #DISPLAY and it also slows the speed of tracking

rear_wheels_enable  = True
front_wheels_enable = True

PAN_ANGLE_MAX   = 170
PAN_ANGLE_MIN   = 10
TILT_ANGLE_MAX  = 150
TILT_ANGLE_MIN  = 70
FW_ANGLE_MAX    = 90+30
FW_ANGLE_MIN    = 90-30

bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)
picar.setup()

fw.offset = 0
pan_servo.offset = 10
tilt_servo.offset = 0

bw.speed = 0
fw.turn(90)
pan_servo.write(90)
tilt_servo.write(90)

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
                bw.forward()
                sleep(0.01)

            # Atrás
            for x in range(100):
                bw.speed = motor_speed
                bw.backward()
                sleep(0.01)

            # Izquierda?
            if front_wheels_enable:

                for lado in range(4):
                    fw_angle = 180 - (lado * 45)

                    for x in range(100):
                        fw.turn(fw_angle)
                        bw.speed = motor_speed
                        bw.forward()
                        sleep(0.01)
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