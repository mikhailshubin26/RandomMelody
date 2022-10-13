import sqlite3
from play import play

def open():
    con = sqlite3.connect('records.db')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM recs""").fetchall()
    for elem in result:
        print(elem)

    cl = input('Type Anything to close:     ').title()
    if cl.isdigit():
        cl = int(cl)
        for elem in result:
            if elem[0] == cl:
                instr = elem[6]
                notess = elem[4]
                lenght = elem[3]
                break
            else:
                continue
        notess = notess.split('; ')
        print(notess)
        for elem in notess:
            if elem != notess[-1]:
                try:
                    play(instr, elem)
                except FileNotFoundError:
                    print('Ошибка 2.1:\nФайл был сохранён неверно')
                    break
                continue
            else:
                break
    else:
        pass