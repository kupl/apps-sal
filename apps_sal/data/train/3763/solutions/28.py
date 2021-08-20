def calculator(x, y, op):
    if op in ('+', '-', '*', '/') and type(x) == int and (type(y) == int):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return x / y
    else:
        return 'unknown value'
