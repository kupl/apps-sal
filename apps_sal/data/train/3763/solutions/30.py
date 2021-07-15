def calculator(x,y,op):
    print (f"{x}{op}{y}")
    try:
         if op in "+-/*":
            return eval(f"{x}{op}{y}")
    except:
        pass
    return "unknown value"    
