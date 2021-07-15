import operator
ops = {"+": operator.add, "-": operator.sub,  "*": operator.mul, "/": operator.truediv}

def calculator(x,y,op):
    print(op)
    print(x)
    print(y)
    return ops[op](x, y) if op in ops.keys() and str(x).isnumeric() and str(y).isnumeric() else "unknown value"
