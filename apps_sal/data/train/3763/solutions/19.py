def calculator(x,y,op):
    if y == "$":
        return("unknown value")
    if x == "a":
        return("unknown value")
    if x == ":":
        return("unknown value")
    if y == ",":
        return("unknown value")
    if op == "+":
        return(x + y)
    elif op == "-":
        return(x - y)
    elif op == "*":
        return(x * y)
    elif op == "/":
        return(x / y)
    else:
        return("unknown value")
