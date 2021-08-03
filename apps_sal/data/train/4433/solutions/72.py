from functools import reduce


def logical_calc(array, op):
    return {
        'AND': all(array),
        'OR': any(array),
        'XOR': reduce(lambda x, y: x ^ y, array)
    }.get(op)
