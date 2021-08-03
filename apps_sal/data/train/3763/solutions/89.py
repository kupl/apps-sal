def calculator(x, y, op):
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            return "unknown value"
        if (op == '+'):
            return x + y
        elif (op == '-'):
            return x - y
        elif (op == '*'):
            return x * y
        elif (op == '/'):
            return x / y
        else:
            return "unknown value"
    except:
        return "unknown value"
