def calculator(x,y,op):
    ops = '+-*/'
    try: return eval('{}{}{}'.format(x,op,y)) if op in ops else 'unknown value'
    except: return 'unknown value'
