def calculator(x,y,op):
    if not (type(x) == int and type(y)==int):
        return "unknown value"

    if op == '+': return x+y
    elif op == '*': return x*y
    elif op == '-': return x-y
    elif op == '/': return x/y
    else: return "unknown value"

