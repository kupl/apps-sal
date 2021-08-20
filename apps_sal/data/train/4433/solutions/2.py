def logical_calc(array, op):
    ops = {'AND': lambda x, y: x & y, 'OR': lambda x, y: x | y, 'XOR': lambda x, y: x ^ y}
    from functools import reduce
    return reduce(ops[op], array)
