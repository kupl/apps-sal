from functools import reduce


def logical_calc(array, op):
    if op == 'AND':
        value = reduce(lambda x, y: x and y, array)
    elif op == 'OR':
        value = reduce(lambda x, y: x or y, array)
    else:
        value = reduce(lambda x, y: x ^ y, array)
    return value
