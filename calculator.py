import math

# DISPLAY

def display_menu():
    print("\nAdvanced Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Logarithm")
    print("8. Trigonometric Functions")
    print("9. Exit")

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Negative value."

def power(x, y):
    return math.pow(x, y)

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error! Logarithm base or value not valid."

def trigonometric_functions(angle, func_type):
    angle_rad = math.radians(angle)
    if func_type == 'sin':
        return math.sin(angle_rad)
    elif func_type == 'cos':
        return math.cos(angle_rad)
    elif func_type == 'tan':
        return math.tan(angle_rad)
    else:
        return "Error! Invalid function type."

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '9':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
                print(f"The result is: {addition(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {division(num1, num2)}")

        elif choice == '5':
            num = float(input("Enter the number: "))
            print(f"The result is: {square_root(num)}")

        elif choice == '6':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print(f"The result is: {power(base, exponent)}")

        elif choice == '7':
            num = float(input("Enter the number: "))
            base = float(input("Enter the base (default is e): ") or 'e')
            print(f"The result is: {logarithm(num, base)}")

        elif choice == '8':
            angle = float(input("Enter the angle in degrees: "))
            func_type = input("Enter the trigonometric function (sin, cos, tan): ").strip().lower()
            print(f"The result is: {trigonometric_functions(angle, func_type)}")

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
