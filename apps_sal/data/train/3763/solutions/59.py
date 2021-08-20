def calculator(x, y, op):
    if str(x).isnumeric() and str(y).isnumeric() and (op == '+' or op == '*' or op == '/' or (op == '-')):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
    else:
        return 'unknown value'
    pass
