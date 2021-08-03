def calculator(x, y, op):
    try:
        xx = int(x)
        yy = int(y)
    except ValueError:
        return "unknown value"
    if op == '+':
        return xx + yy
    elif op == '-':
        return xx - yy
    elif op == '*':
        return xx * yy
    elif op == '/':
        return xx / yy
    else:
        return "unknown value"
