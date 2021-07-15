def calculator(x,y,op):
    if isinstance(x,int) == True and isinstance(y,int) == True and (isinstance(op,str) == True and op in '+-*/'): 
        if op == '+': return x+y
        elif op == '-': return x-y
        elif op == '*':return x*y
        elif op == '/': return x/y 
    else: return "unknown value"
