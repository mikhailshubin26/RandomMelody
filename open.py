import sqlite3
from play import play

def open():
    con = sqlite3.connect('records.db')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM recs""").fetchall()
    for elem in result:
        print(elem)

    cl = input('Type Anything to close').title()
