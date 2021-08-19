def calculator(x, y, op):
    try:
        if op == '+' and type(x) == int and (type(y) == int):
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return 'unknown value'
    except TypeError:
        return 'unknown value'
