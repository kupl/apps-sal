from functools import reduce


def logical_calc(array, op):
    if op == 'AND':

        def l(x, y):
            return x and y
    elif op == 'OR':

        def l(x, y):
            return x or y
    else:

        def l(x, y):
            return x ^ y
    return reduce(l, array)
