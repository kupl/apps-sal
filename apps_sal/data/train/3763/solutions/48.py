def calculator(x, y, op):
    if str(x).isnumeric() and str(y).isnumeric():
        if op == '+':
            res = x + y
            return res
        if op == '-':
            res = x - y
            return res
        if op == '*':
            res = x * y
            return res
        if op == '/':
            res = x / y
            return res
    return "unknown value"
