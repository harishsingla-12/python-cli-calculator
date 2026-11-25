def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return "Invalid operator."

if __name__ == "__main__":
    print("=== CLI Calculator v1.1 (Add, Subtract, Multiply) ===")
    x = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *): ").strip()
    y = float(input("Enter second number: "))
    print("Result:", calculate(x, y, op))