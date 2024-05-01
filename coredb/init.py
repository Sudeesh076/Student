import sqlite3


def startDb():
    db = sqlite3.connect("student.db")
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    create_users_table(cursor)
    create_subject_table(cursor)
    db.commit()
    db.close()


def create_users_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE users")

    cursor.execute('''CREATE TABLE users (
        id TEXT PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        ph_number TEXT,
        type TEXT,
        course TEXT
    )''')

def create_subject_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='subject'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE subject")

    cursor.execute('''CREATE TABLE subject (
        id TEXT PRIMARY KEY,
        subject TEXT,
        semester TEXT,
        Description TEXT,
        course TEXT
    )''')
