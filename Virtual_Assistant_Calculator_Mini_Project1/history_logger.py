python
CopyEdit
import sqlite3
import os

DB_NAME = "history.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                            id INTEGER PRIMARY KEY,
                            operand1 REAL,
                            operand2 REAL,
                            operation TEXT,
                            result REAL
                          )''')
        conn.commit()

def log_operation(a, b, op, result):
    init_db()
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (operand1, operand2, operation, result) VALUES (?, ?, ?, ?)",
                       (a, b, op, result))
        conn.commit()
