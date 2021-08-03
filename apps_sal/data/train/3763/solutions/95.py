def calculator(x, y, op):
    if str(op) not in '+-*/' or str(x) not in '0123456789' or str(y) not in '0123456789':
        return "unknown value"
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    else:
        return x / y
