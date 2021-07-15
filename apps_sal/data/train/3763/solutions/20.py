def calculator(x,y,op,msg='unknown value'):
    try:
        return eval(str(x)+op+str(y)) if op in '+-*/' else msg
    except:
        return msg
