import re

def calculator(x,y,op):
    if re.match('[-\+\*/]', str(op)) and isinstance(x, int) and isinstance(y, int):
        return eval(str(x) + op + str(y))
    else:
        return "unknown value"
