from operator import add, sub, mul, truediv as div


def WRONG_FUNC(x, y):
    return 'unknown value'


def calculator(x, y, op):
    validOp = op if all((isinstance(v, int) for v in (x, y))) else '!'
    return {'+': add, '-': sub, '*': mul, '/': div}.get(validOp, WRONG_FUNC)(x, y)
