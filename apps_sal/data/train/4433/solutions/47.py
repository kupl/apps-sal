from functools import reduce


def logical_calc(array, op):
    operators = {
        'AND': all(array),
        'OR': any(array),
        'XOR': reduce(lambda x, y: x ^ y, array)
    }
    return operators[op]
