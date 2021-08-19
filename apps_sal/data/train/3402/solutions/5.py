def calculate(a, o, b):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif b != 0 and o == '/':
        return a / b
    elif o == '*':
        return a * b
    return None
