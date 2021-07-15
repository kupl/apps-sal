def calculator(x,y,op):
    try:
        if op in "+-*/":
            return eval(f"{x} {op} {y}")
        else:
            return "unknown value"
    except:
        return "unknown value"
