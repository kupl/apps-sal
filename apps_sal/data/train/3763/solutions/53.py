def calculator(x, y, op):
    if type(x) != int or type(y) != int or str(op) not in ("+-*/"):
        return "unknown value"

    elif op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return round(x / y, 2)
