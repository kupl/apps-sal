def calculator(x, y, op):
    if type(x) != int or type(y) != int:
        return "unknown value"
    else:
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y
        else:
            return "unknown value"

    pass
