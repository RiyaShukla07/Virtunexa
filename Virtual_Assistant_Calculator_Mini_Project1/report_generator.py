python
CopyEdit
import pandas as pd
import sqlite3

def generate_report():
    conn = sqlite3.connect("history.db")
    df = pd.read_sql_query("SELECT * FROM history", conn)
    df.to_csv("calculation_report.csv", index=False)
    conn.close()
