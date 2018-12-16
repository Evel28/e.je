import sqlite3

conn = sqlite3.connect('datos.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Data_sql (title TEXT, plays INTEGER)')

conn.close()