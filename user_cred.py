import sqlite3

'''
Create a SQLite3 database and table

'''

conn = sqlite3.connect('user_credentials.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        username TEXT UNIQUE,\
        password TEXT)\
              ")

conn.commit()

