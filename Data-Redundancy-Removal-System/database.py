import sqlite3
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        phone TEXT,
        department TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_employee(name, email, phone, department):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees(name,email,phone,department)
    VALUES(?,?,?,?)
    """, (name, email, phone, department))

    conn.commit()
    conn.close()

def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    conn.close()
    return data

def email_exists(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE email=?",
        (email,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None