def calculator(x, y, op):
    valid_operators = ['+', '-', '*', '/']
    if op in valid_operators and str(x).isnumeric() and str(y).isnumeric():
        return eval(str(x) + op + str(y))
    else:
        return 'unknown value'
