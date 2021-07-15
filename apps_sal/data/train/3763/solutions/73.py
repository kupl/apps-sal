def calculator(x,y,op):
    if type(x)==str or type(y)==str or op not in ["+", "-", "*", "/"]:
        return "unknown value"
    else:
        if op=="+":
            return x+y 
        if op=="-":
            return x-y
        if op=="*":
            return x*y
        if op=="/":
            return x/y
