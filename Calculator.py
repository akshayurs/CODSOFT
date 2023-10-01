def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operator == '%':
        if b != 0:
            return a % b
        else:
            return "Error: Modulo by zero"
    elif operator == '^':
        return a ** b
    else:
        return "Invalid operator. Please enter one of the supported operators: +, -, /, *, %, ^"


print("Calculator")
a = float(input("Enter a : "))
b = float(input("Enter b : "))
opt = input("Enter the operator (+, -, /, *, %, ^): ")

result = calculate(a, b, opt)

if isinstance(result, str):
    print(result)
else:
    print(f"Result: {result}")
