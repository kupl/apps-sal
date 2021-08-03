import operator as ops


def calculator(x, y, op):
    try:
        return {'+': ops.add(x, y), '-': ops.sub(x, y), '*': ops.mul(x, y), '/': ops.truediv(x, y)}.get(op, "unknown value")
    except:
        return "unknown value"
