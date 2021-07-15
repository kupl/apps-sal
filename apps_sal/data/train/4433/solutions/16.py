from functools import reduce

def logical_calc(array, op):
    if op == 'AND':
        return reduce(lambda x, y: x and y, array)
    elif op == 'OR':
        return reduce(lambda x, y: x or y, array)
    elif op == 'XOR':
        return reduce(lambda x, y: x != y, array)
