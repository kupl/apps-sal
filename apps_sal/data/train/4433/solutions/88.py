from functools import reduce


def logical_calc(array, op):
    if op == 'AND':
        l = lambda x, y: x and y
    elif op == 'OR':
        l = lambda x, y: x or y
    else:
        l = lambda x, y: x ^ y
    return reduce(l, array)
