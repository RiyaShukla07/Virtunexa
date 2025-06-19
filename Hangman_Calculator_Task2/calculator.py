import sqlite3 
import logging 
 
logging.basicConfig(filename='calc_operations.log', level=logging.INFO, 
format='%(asctime)s - %(message)s') 
 
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
 
def calculator(): 
    print(" Welcome to the Python Calculator!") 
    while True: 
        try: 
            a = float(input("Enter first number: ")) 
            op = input("Enter operator (+, -, *, /): ") 
            b = float(input("Enter second number: ")) 
 
            if op == '+': 
                result = a + b 
            elif op == '-': 
                result = a - b 
            elif op == '*': 
                result = a * b 
            elif op == '/': 
                if b == 0: 
                    raise ZeroDivisionError("Cannot divide by zero.") 
                result = a / b 
            else: 
                print("Invalid operator.\n") 
                continue 
 
            print(f"Result: {result}\n") 
            expression = f"{a} {op} {b}" 
            logging.info(f"{expression} = {result}") 
            save_to_db(expression, str(result)) 
 
        except ValueError: 
            print(" Invalid input. Please enter numeric values.\n") 
        except ZeroDivisionError as e: 
            print(f" Error: {e}\n") 
 
        again = input("Do another calculation? (y/n): ").lower() 
        if again != 'y': 
            break 
 
    conn.close() 
 
if __name__ == "__main__": 
    calculator()
