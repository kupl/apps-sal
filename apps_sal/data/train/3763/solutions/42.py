def calculator(x, y, op):
    print((x, y, op))
    if type(x) == str or type(y) == str:
        return 'unknown value'
    elif op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return 'unknown value'
