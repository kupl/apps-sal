def calculator(x, y, op):
    return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'
