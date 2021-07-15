def calculator(x,y,op):
    if (type(x) is int and type(y) is int and type (op) is str):
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x/y
        else:
            return "unknown value"
    else:
        return "unknown value"
