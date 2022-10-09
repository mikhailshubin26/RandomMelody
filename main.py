import random


from note_list import note_list
from play import play
from save import save
from open import open

import pygame




pygame.init()
while True:
    start = input('What do you want to do (Create, Open):   ').title()
    if start == "Open":
        open()

    mode = input("Choose the mode (Loop, Usual):    ").title()

    lst_tune = ["С", "Cm", "C#", "C#m", "D", "Dm", "D#", "D#m", "E", "Em", "F", "Fm", "F#", "F#m", "G", "Gm", "G#", "G#m", "A",
           "Am", "A#", "A#m", "B", "Bm", "Random"]

    lst_instr = ['Piano', 'Guitar', 'Brass', 'Bass']

    tune = input("Сhoose the tune:\n"
                 "С, Cm, C#, C#m,\n"
                 "D, Dm, D#, D#m,\n"
                 "E, Em, F, Fm,\n"
                 "F#, F#m, G, Gm,\n"
                 "G#, G#m, A, Am,\n"
                 "A#, A#m, B, Bm,\n"
                 "Random\n").title()


    lenght = int(input("Choose the melody lenght in notes (8; 16; 32, 64, 128, 256): "))

    instr = input("Выбери инструмент: Piano, Guitar, Brass, Bass, Random:    ").title()

    if tune == 'Random':
        tune = random.randint(0, len(lst_tune) - 1)
        tune = lst_tune[tune]
        print(tune)

    if instr == 'Random':
        instr = random.randint(0, len(lst_instr) - 1)
        instr = lst_instr[instr]

    notes = []
    notes = note_list(tune)

    melody = []
    if lenght <= 16 or mode == 'Usual':
        for i in range(lenght):
            melody.append(notes[random.randint(0, len(notes) - 1)])
    else:
        for i in range(16):
            melody.append(notes[random.randint(0, len(notes) - 1)])

    print(f"{tune}; {instr}")
    print(melody)

    if lenght <= 16 or mode == 'Usual':
        for elem in melody:
            play(instr, elem)

    else:
        for i in range(lenght // 16):
            for elem in melody:
                play(instr, elem)

    cont = input("Continue; Break; Save:    ").title()
    if cont == 'Countinue':
        continue
    elif cont == 'Break':
        print('Goodbye')
        break
    elif cont == 'Save':
        name = input("Name:     ")
        save(name, tune, lenght, melody, instr)

pygame.quit
