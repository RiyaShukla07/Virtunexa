import tkinter as tk 
import sqlite3 
 
conn = sqlite3.connect('calc_history.db') 
cursor = conn.cursor() 
cursor.execute('''CREATE TABLE IF NOT EXISTS history ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    expression TEXT NOT NULL, 
    result TEXT NOT NULL 
)''') 
conn.commit() 
 
def save_to_db(expression, result): 
    cursor.execute("INSERT INTO history (expression, result) VALUES (?, ?)", (expression, 
result)) 
    conn.commit() 
 
root = tk.Tk() 
root.title("Python GUI Calculator") 
expression = "" 
 
def press(num): 
    global expression 
    expression += str(num) 
    equation.set(expression) 
 
def equalpress(): 
    global expression 
    try: 
        total = str(eval(expression)) 
        equation.set(total) 
        save_to_db(expression, total) 
        expression = "" 
    except: 
        equation.set("Error") 
        expression = "" 
 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
 
equation = tk.StringVar() 
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 18), bd=10, insertwidth=2, 
width=14, borderwidth=4) 
entry_field.grid(columnspan=4) 
 
buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+'] 
row = 1 
col = 0 
 
for button in buttons:
