def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Function to get a valid numeric input from the user
def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Main program
num1 = get_numeric_input("Enter the first number: ")
operation = input("Enter the operation (+, -, *, /): ")
num2 = get_numeric_input("Enter the second number: ")

while True:
    add_another_num = input("Would you like to add another number? (yes or no): ").lower()

    if add_another_num == "yes":
        num3 = get_numeric_input("Enter the next number: ")
        num1 = add(num1, num3) if operation == '+' else subtract(num1, num3) if operation == '-' else multiply(num1, num3) if operation == '*' else divide(num1, num3)
    elif add_another_num == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Perform the final calculation based on the chosen operation
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
