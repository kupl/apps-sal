def calculator(x,y,op):
    return eval('{}{}{}'.format(x, op, y)) if op in ['+', '-', '*', '/'] and isinstance(x, int) and isinstance(y, int) else "unknown value"
