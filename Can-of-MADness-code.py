# ! /usr/bin/python3

from gpiozero import Button
import pygame
import glob
import random
from time import sleep

sampleplay = Button(3)
soundfiles = glob.glob("/home/pi/musicbox/samples/*.wav")

pygame.init()
pygame.mixer.init()

while True:
    sampleplay.wait_for_press()
    sample = pygame.mixer.Sound(random.choice(soundfiles))
    sample.play()
    sleep(10)
    sample.stop()