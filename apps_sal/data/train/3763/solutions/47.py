def calculator(x,y,op):
    return eval(f'{x}{op}{y}') if str(op) in "+-*/" and type(x) == type(y) == int else "unknown value"
