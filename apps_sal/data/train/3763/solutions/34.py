def calculator(x,y,op):
    if type(x) == int and type(y) == int and str(op) in '*/-+':
        return eval(f'{x}{op}{y}')
    else:
        return 'unknown value'
    
    return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'
