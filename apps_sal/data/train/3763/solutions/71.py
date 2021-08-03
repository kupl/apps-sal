def calculator(x, y, op):
    if op == "+":
        try:
            return int(x + y)
        except:
            return "unknown value"
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        return "unknown value"
