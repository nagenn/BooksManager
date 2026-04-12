#This handles the database aspect of the book manager app
import sqlite3

DB_NAME = "books.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        status TEXT DEFAULT 'unread'
    )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO users(username,password) VALUES('admin','admin')"
    )

    conn.commit()
    conn.close()
