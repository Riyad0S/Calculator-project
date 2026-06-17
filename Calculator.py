# Custom exception created to handle invalid operations
class OperationException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
# -----------------------------------

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2
# --------------------------------

while True:
    try:
        operation = input("choose the operation '+' '*' '-' '/' or '0' to exit: ")

        if operation not in ("+", "-", "*", "/", "0"):
                raise OperationException("Invalid operation.")
    except OperationException as e:
        print(e)
        continue

    if operation == "0":
        print("Thank you for using this program and goodbye!")
        break

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("input must be a number.")
        continue

    if operation == "+":
        print(f"{num1} + {num2} = {addition(num1, num2)}")

    elif operation == "-":
        print(f"{num1} - {num2} = {subtraction(num1, num2)}")

    elif operation == "*":
        print(f"{num1} x {num2} = {multiplication(num1, num2)}")

    elif operation == "/":
        try:
            print(f"{num1} / {num2} = {division(num1, num2)}")
        except ZeroDivisionError:
            print("Division by zero is not permissible.")