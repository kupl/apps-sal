def calculator(x, y, op):
    print(x, y, type(x), type(y))
    if op == '+' and type(x) == type(y) == int:
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y
    elif op == '*':
        return x * y
    else:
        return 'unknown value'
