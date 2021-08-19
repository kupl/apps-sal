def calculator(x, y, op):
    print((x, y, op))
    if op == '+' and type(x) == type(y) == int:
        return x + y
    elif op == '-' and type(x) == type(y) == int:
        return x - y
    elif op == '*' and type(x) == type(y) == int:
        return x * y
    elif op == '/' and type(x) == type(y) == int:
        return x / y
    else:
        return 'unknown value'
