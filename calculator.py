def base_arithmetic(n1, op, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

def exponents(n1, n2):
    return n1 ** n2

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

print("Calculator Menu:")
print("1. Basic arithmetic")
print("2. Exponent calculation")

op_selection = input("Enter your choice (1 or 2): ")

if op_selection == "1":
    n1 = get_float_input("Enter the first number: ")
    op = input("Enter the operation (+, -, *, /): ")
    n2 = get_float_input("Enter the second number: ")
    result = base_arithmetic(n1, op, n2)
    print("Result:", result)
elif op_selection == "2":
    base = get_int_input("Enter the base number: ")
    exponent = get_int_input("Enter the exponent: ")
    result = exponents(base, exponent)
    print("Result:", result)
else:
    print("Invalid choice! Please enter 1 or 2.")
