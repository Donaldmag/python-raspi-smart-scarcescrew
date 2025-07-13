from gpiozero import MotionSensor
# import pygame
from time import sleep

pir = MotionSensor(23)
#speaker = DigitalOutputDevice(18)

while True:
        pir.wait_for_motion()
        print("✅ Motion detected!")
