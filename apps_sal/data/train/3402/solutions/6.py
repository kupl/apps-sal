def calculate(a, o, b):
    return eval(str(a) + o + str(b)) if o in '+-/*' and o + str(b) != '/0' else None
