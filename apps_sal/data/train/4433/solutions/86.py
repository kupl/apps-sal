from functools import reduce

def logical_calc(array, op):
    return {
        'AND': reduce(lambda x, y: x & y, array),
        'OR': reduce(lambda x, y: x | y, array),
        'XOR': reduce(lambda x, y: x ^ y, array)
    }.get(op)
