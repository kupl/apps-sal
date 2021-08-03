def calculator(x, y, op):
    try:
        if op == '+':
            return int(x) + int(y)
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return 'unknown value'
    except:
        return 'unknown value'
