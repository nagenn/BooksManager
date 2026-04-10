
from db import get_connection

def authenticate(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password),
    )

    user = cursor.fetchone()
    conn.close()

    return user

def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_book(title, author):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO books(title, author) VALUES ('{title}','{author}')"

    cursor.execute(query)

    conn.commit()
    conn.close()
