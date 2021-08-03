from functools import reduce


def logical_calc(array, op):
    if op == 'AND':
        return reduce((lambda x, y: x and y), array)
    elif op == 'OR':
        return reduce((lambda x, y: x or y), array)
    else:
        return reduce((lambda x, y: x ^ y), array)
# This one fucked my mind for two days & here i got then! :p
# Completed by Ammar on 1/8/2019 at 09:51PM.
