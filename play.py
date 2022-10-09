import pygame

from time import sleep

def play(instr, elem):
    sound = pygame.mixer.Sound(f'sounds/{instr}/{instr}{elem}.wav')
    pygame.mixer.Sound.play(sound)
    if instr == 'Piano':
        sleep(0.3)
    if instr == 'Guitar':
        sleep(0.2)
    if instr == 'Brass':
        sleep(0.25)
    if instr == 'Bass':
        sleep(0.5)