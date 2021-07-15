def logical_calc(array, op):
    return {'AND': all, 'OR': any, 'XOR': lambda a: sum(a) % 2}[op](array)
