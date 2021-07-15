def calculator(x,y,op,check='+-*/'):
    try:
        return eval(str(x)+op+str(y)) if op in check else 'unknown value'
    except:
        return 'unknown value'
