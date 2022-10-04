import random
import os
import sys
from note_list import note_list
from time import time, sleep
import pygame



pygame.init()

lst_tune = ["С", "Cm", "C#", "C#m", "D", "Dm", "D#", "D#m", "E", "Em", "F", "Fm", "F#", "F#m", "G", "Gm", "G#", "G#m", "A",
       "Am", "A#", "A#m", "B", "Bm", "B#", "B#m", "Random"]

lst_instr = ['Piano', 'Guitar', 'Brass']

tune = input("Выберите тональность:\n"
             "С, Cm, C#, C#m,\n"
             "D, Dm, D#, D#m,\n"
             "E, Em, F, Fm,\n"
             "F#, F#m, G, Gm,\n"
             "G#, G#m, A, Am,\n"
             "A#, A#m, B, Bm,\n"
             "B#, B#m, Random\n").title()

lenght = int(input("Введите длину мелодии в нотах (8; 16; 32): "))

instr = input("Выбери инструмент: Piano, Guitar, Brass, Random:    ").title()

if tune == 'Random':
    tune = random.randint(0, len(lst_tune) - 1)
    tune = lst_tune[tune]

if instr == 'Random':
    instr = random.randint(0, len(lst_instr) - 1)
    instr = lst_instr[instr]

notes = []
notes = note_list(tune)

melody = []
for i in range(lenght):
    melody.append(notes[random.randint(0, len(notes) - 1)])

print(tune)
print(melody)

for elem in melody:
    sound = pygame.mixer.Sound(f'sounds/{instr}/{instr}{elem}.wav')
    pygame.mixer.Sound.play(sound)
    if instr == 'Piano':
        sleep(0.3)
    if instr == 'Guitar':
        sleep(0.2)
    if instr == 'Brass':
        sleep(0.25)

pygame.quit