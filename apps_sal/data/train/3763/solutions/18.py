def calculator(x,y,op):
    try:
        if op in '+-*/':
            return eval(f'{x}{op}{y}')
    except:
        pass
    return 'unknown value'
