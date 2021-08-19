import functools


def logical_calc(array, op):
    return {'AND': all, 'OR': any, 'XOR': xor}[op](array)


def xor(array):
    return functools.reduce(lambda x, y: x != y, array)
