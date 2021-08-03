def calculator(x, y, op):
    try:
        x = int(x)
        y = int(y)
    except:
        return 'unknown value'
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    return 'unknown value'
