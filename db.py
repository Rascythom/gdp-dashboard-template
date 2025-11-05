import sqlite3

def get_connection():
    conn = sqlite3.connect("data/betmastery.db", check_same_thread=False)
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()

    # Tabulka uživatelů
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password_hash TEXT
        )
    ''')

    # Tabulka tiketů
    c.execute('''
        CREATE TABLE IF NOT EXISTS bets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            stake REAL,
            odds REAL,
            result INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()
