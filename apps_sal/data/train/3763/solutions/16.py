def calculator(x, y, op):
    if isinstance(x, int) and isinstance(y, int):
        if op == '+':
            return x + y
        if op == '-':
            return x - y
        if op == '*':
            return x * y
        if op == '/':
            return x / y
    return 'unknown value'
