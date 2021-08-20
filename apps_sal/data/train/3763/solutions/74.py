def calculator(x, y, op):
    if isinstance(x, int) == True and isinstance(y, int) == True and (op in ['+', '-', '*', '/']):
        if op == '+':
            return x + y
        if op == '-':
            return x - y
        if op == '*':
            return x * y
        if op == '/':
            return x / y
    else:
        return 'unknown value'
