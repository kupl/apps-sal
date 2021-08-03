import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calculator(x, y, op):
    try:
        if isinstance(x, int) and isinstance(y, int):
            return ops.get(op)(x, y)
        return "unknown value"
    except:
        return "unknown value"
