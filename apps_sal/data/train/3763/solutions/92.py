def calculator(x, y, op):
    if op in ['+', '-', '*', '/'] and type(x) is int and (type(y) is int):
        finalStr = str(x) + op + str(y)
        return eval(finalStr)
    else:
        return 'unknown value'
