def calculator(x,y,op):
    try:
        if op in '+-/*':
            return eval(str(x)+op+str(y))
        else:
            return 'unknown value'
    except:
        return 'unknown value'
