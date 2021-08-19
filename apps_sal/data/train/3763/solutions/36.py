def calculator(x, y, op):
    if op == '+' and type(x) is int and (type(y) is int):
        return x + y
    elif op == '-' and type(x) is int and (type(y) is int):
        return x - y
    elif op == '*' and type(x) is int and (type(y) is int):
        return x * y
    elif op == '/' and type(x) is int and (type(y) is int):
        return int(x) / int(y)
    else:
        return 'unknown value'
