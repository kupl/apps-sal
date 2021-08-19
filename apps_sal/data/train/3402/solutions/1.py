def calculate(a, o, b):
    result = 0
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '/' and b == 0:
        return None
    elif o == '/':
        return a / b
    elif o == '*' and b == 0:
        return b
    elif o == '*':
        return a * b
    else:
        return None
    return result
