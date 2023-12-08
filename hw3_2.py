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
        return "cannot be divided by zero"

operator = input("enter the operator (+, -, *, /:) ")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operator"

print(f"Result: {result}")