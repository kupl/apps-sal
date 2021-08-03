def calculator(x, y, op):
    if not isinstance(x, int) or not isinstance(y, int):
        return 'unknown value'

    if op == '+':
        return x + y

    if op == '-':
        return x - y

    if op == '*':
        return x * y

    if op == '/':
        return x / y

    return 'unknown value'
