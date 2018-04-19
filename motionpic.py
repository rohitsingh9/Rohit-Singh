import os
import time
from gpiozero import MotionSensor
pir=MotionSensor(4)
img="/home/pi/cam/img.jpg"

def mypic():
    cmd="fswebcam-FS--fps20-r\"1200x800
    os.system(cmd)
    print("pic taken")

    while True:
        if pir.motion_detected:
            mypic()
