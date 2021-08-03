import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calculator(x, y, op):
    try:
        return ops[op](int(x), int(y))
    except (ValueError, KeyError):
        return 'unknown value'
