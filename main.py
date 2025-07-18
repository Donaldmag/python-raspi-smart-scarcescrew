from gpiozero import MotionSensor, TonalBuzzer
# import pygame
from time import sleep

pir = MotionSensor(23)
buzzer = TonalBuzzer(18)
# pygame.mixer.init()
# pygame.mixer.music.load("/static/sounds/alert.wav")

print("Waiting for motion...")
while True:
        pir.wait_for_motion()
        print("✅ Motion detected!")

        buzzer.play(440)
        sleep(1)
        buzzer.stop()