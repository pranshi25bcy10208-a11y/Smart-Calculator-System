import math

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def sqrt(n1, _):
    return math.sqrt(n1)

def logarithm(n1, _):
    return math.log10(n1)

def natural_log(n1, _):
    return math.log(n1)

def sine(n1, _):
    return math.sin(math.radians(n1))

def cosine(n1, _):
    return math.cos(math.radians(n1))

def tangent(n1, _):
    return math.tan(math.radians(n1))

def factorial(n1, _):
    return math.factorial(int(n1))


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "√": sqrt,
    "log": logarithm,
    "ln": natural_log,
    "sin": sine,
    "cos": cosine,
    "tan": tangent,
    "!": factorial,
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol in ["√", "log", "ln", "sin", "cos", "tan", "!"]:
            num2 = 0  # dummy value
        else:
            num2 = float(input("What is the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2 if num2 != 0 else ''} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
