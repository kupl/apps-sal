from functools import reduce


def logical_calc(array, op):
    if op == 'AND':
        return reduce(lambda a, b: a and b, array)
    if op == 'OR':
        return reduce(lambda a, b: a or b, array)
    return reduce(lambda a, b: a ^ b, array)
