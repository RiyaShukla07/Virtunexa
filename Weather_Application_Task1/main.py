from weather_api import get_weather
from calculator import add, subtract, multiply, divide

def main():
    api_key = "YOUR_API_KEY_HERE"
    while True:
        print("\nChoose an option:")
        print("1. Get Weather")
        print("2. Calculator")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            try:
                weather = get_weather(city, api_key)
                print(f"Temperature: {weather['temperature']}°C")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Wind Speed: {weather['wind_speed']} m/s")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ")

            try:
                if op == '+':
                    print("Result:", add(a, b))
                elif op == '-':
                    print("Result:", subtract(a, b))
                elif op == '*':
                    print("Result:", multiply(a, b))
                elif op == '/':
                    print("Result:", divide(a, b))
                else:
                    print("Invalid operator.")
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            break
        else:
            print("Invalid choice.")
