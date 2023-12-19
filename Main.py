# Function to perform addition
def add(x, y, z=None):
    if z is not None:
        return x + y + z
    else:
        return x + y

# Function to perform subtraction
def subtract(x, y, z=None):
    if z is not None:
        return x - y - z
    else:
        return x - y

# Function to perform multiplication
def multiply(x, y, z=None):
    if z is not None:
        return x * y * z
    else:
        return x * y

# Function to perform division
def divide(x, y, z=None):
    if z is not None and z != 0:
        return x / y / z
    elif z == 0:
        return "Error: Division by zero"
    else:
        return x / y

# Take  in the first , second, & the operation, then asks if the user would like to add another number.
# The anwsers yes/no are not case sensitive.
num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
AddAnothernum = input("Would you like to add another number? (yes or no): ")

# Converts input to lowercase for case-insensitivity
AddAnothernum = AddAnothernum.lower()

# Perform calculation based on the chosen operation and the user's decision to add another number or not.
if AddAnothernum == "yes":
    num3 = float(input("Enter the third number: "))
    if any(map(lambda x: x.isalpha(), [num1, num2, num3])):
        result = "Please enter valid numbers only for all inputs."
    else:
        if operation == '+':
            result = add(num1, num2, num3)
        elif operation == '-':
            result = subtract(num1, num2, num3)
        elif operation == '*':
            result = multiply(num1, num2, num3)
        elif operation == '/':
            result = divide(num1, num2, num3)
        else:
            result = "Error: Invalid operation"
else:
    if any(map(lambda x: x.isalpha(), [num1, num2])):
        result = "Please enter valid numbers only for all inputs."
    else:
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Error: Invalid operation"

# Display the result
print(f"Result: {result}")
