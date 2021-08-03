import operator as op

f = {
    "add": op.add,
    "subtract": op.sub,
    "multiply": op.mul,
    "divide": op.truediv
}


def arithmetic(a, b, operator):
    return f[operator](a, b)
