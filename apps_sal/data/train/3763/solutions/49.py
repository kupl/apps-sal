def calculator(x, y, op):
    if type(op) == str and op in "+-*/" and type(x) == int and type(y) == int:
        calc = str(x) + op + str(y)
        return eval(calc)
    else:
        return "unknown value"
