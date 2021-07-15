def calculator(x,y,op):
    if isinstance(x, int) and isinstance(y, int) and isinstance(op, str) and op in '+-*/':
        return eval(str(x) + op + str(y))
    else:
        return 'unknown value'
