def calculator(x,y,op):
    if (False == isinstance(x, int)) or (False == isinstance(y, int)):
        return "unknown value"
    if "+" == op:
        return x+y
    if "-" == op:
        return x-y
    if "*" == op:
        return x*y
    if "/" == op:
        return x/y
    return "unknown value"
