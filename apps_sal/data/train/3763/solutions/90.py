from numbers import Number
def calculator(x,y,op):
    if type(x) == int and type(y) == int and op == "+":
        return x + y
    elif type(x) == int and type(y) == int and op == "-":
        return x - y
    elif type(x) == int and type(y) == int and op == "*":
        return x * y
    elif type(x) == int and type(y) == int and op == "/":
        return x / y
    if type(x) == int and type(y) == int or (op != "+" or "-" or "*" or "/"):
        return "unknown value"
    pass
