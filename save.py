import sqlite3
from datetime import datetime
from time import sleep

def save(name, tune, lenght, melody, instr):
    mel = ''
    for e in melody:
        mel += f'{e}; '

    con = sqlite3.connect('records.db')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM recs""").fetchall()
    while True:
        if name in result:
            print("Имя занято")
            name = input("Name:     ")
        else:
            break
    cur.execute(f"INSERT INTO recs (name, date, lenght, melody, tune, instr) VALUES ('{name}', '{datetime.now()}', '{lenght}', '{mel}', '{tune}', '{instr}')")
    con.commit()
    cur.close()
    con.close()
    for i in range(0, 101):
        print(f'{i}%')
        sleep(0.01)

