python
CopyEdit
from weather_api import get_weather
from calculator import add, subtract, multiply, divide
from history_logger import log_operation
from report_generator import generate_report

def main():
    api_key = "YOUR_API_KEY_HERE"

    while True:
        print("\n Choose an option:")
        print("1. Get Weather")
        print("2. Calculator")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            try:
                weather = get_weather(city, api_key)
                print(f" Temperature: {weather['temperature']}°C")
                print(f" Humidity: {weather['humidity']}%")
                print(f" Wind Speed: {weather['wind_speed']} m/s")
            except Exception as e:
                print(" Error:", e)

        elif choice == "2":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                op = input("Enter operation (+, -, *, /): ")

                result = None
                if op == '+':
                    result = add(a, b)
                elif op == '-':
                    result = subtract(a, b)
                elif op == '*':
                    result = multiply(a, b)
                elif op == '/':
                    result = divide(a, b)
                else:
                    print("Invalid operator.")
                    continue

                print(" Result:", result)
                log_operation(a, b, op, result)

            except Exception as e:
                print(" Error:", e)

        elif choice == "3":
            generate_report()
            print(" Report generated successfully.")

        elif choice == "4":
            print(" Exiting...")
            break
        else:
            print(" Invalid choice.")
