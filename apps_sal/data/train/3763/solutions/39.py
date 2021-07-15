def calculator(x,y,op):
    ops = ("+", "-", "*", "/")
    
    if op in ops and (type(x) == int and type(y) == int):
        return eval(f"{x} {op} {y}")
    
    else:
        return "unknown value"
