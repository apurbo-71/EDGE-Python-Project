# Importing math module

import math


# for summation
def add(a, b):
    return a + b


# for subtraction
def subtract(a, b):
    return a - b


# for multiplication
def multiply(a, b):
    return a * b


# for divition
def divide(a, b):
    if b == 0:
        return "error"
    return a / b


# for exponential
def exponential(a, b):
    return a ** b


# for logarithm
def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        return "error"
    return math.log(a, b)


# for square root
def square_root(a):
    if a < 0:
        return "error"
    return math.sqrt(a)


# for factorial
def factorial(a):
    if a < 0 or not a.is_integer():
        return "error"
    return math.factorial(int(a))


# for remainder
def modulo(a, b):
    return a % b


# for absolute value
def absolute_value(a):
    return abs(a)


# history tracking
calculation_history = []


def history(operation, a, b, result):
    if b is not None:
        calculation_history.append(f"{a} {operation} {b} = {result}")
    else:
        calculation_history.append(f"{operation}({a}) = {result}")


# shows the calculation history
def view_history():
    if not calculation_history:
        print("No history available\n")
    else:
        print("\nCalculation History:")
        for entry in calculation_history:
            print(entry)
    print()


# Main program loop
while True:
    print("Advanced Calculator\n")
    print("Choose an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")
    print("6. Logarithm")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Modulo")
    print("10. Absolute Value")
    print("11. View History")
    print("12. Exit")

    # user input
    choice = input("Enter what you want to do (1-12): ")

    if choice not in [str(i) for i in range(1, 13)]:
        print("Enter a number between 1 and 12.\n")
        continue

    if choice in ['1', '2', '3', '4', '5', '6', '9']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"You entered: {num1} and {num2}")

        if choice == '1':
            result = add(num1, num2)
            history("+", num1, num2, result)
        elif choice == '2':
            result = subtract(num1, num2)
            history("-", num1, num2, result)
        elif choice == '3':
            result = multiply(num1, num2)
            history("*", num1, num2, result)
        elif choice == '4':
            if num2 == 0:
                result = "error"
            else:
                result = divide(num1, num2)
            history("/", num1, num2, result)
        elif choice == '5':
            result = exponential(num1, num2)
            history("^", num1, num2, result)
        elif choice == '6':
            result = logarithm(num1, num2)
            history("log", num1, num2, result)
        elif choice == '9':
            result = modulo(num1, num2)
            history("%", num1, num2, result)

        print(f"Result: {result}\n")

    elif choice in ['7', '8', '10']:
        num = float(input("Enter the number: "))
        print(f"You entered: {num}")

        if choice == '7':
            result = square_root(num)
            history("sqrt", num, None, result)
        elif choice == '8':
            result = factorial(num)
            history("factorial", num, None, result)
        elif choice == '10':
            result = absolute_value(num)
            history("abs", num, None, result)

        print(f"Result: {result}\n")

    # history viewing
    elif choice == '11':
        view_history()
    # exit the program
    else:
        print("Exit")
        break
