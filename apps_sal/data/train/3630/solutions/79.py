import operator as o


def arithmetic(a, b, operator):
    ops = {'add': o.add,
           'subtract': o.sub,
           'multiply': o.mul,
           'divide': o.truediv}
    return ops[operator](a, b)
