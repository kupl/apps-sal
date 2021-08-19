from operator import and_, or_, xor
from functools import reduce


def logical_calc(array, op_str):
    op = {'AND': and_, 'OR': or_, 'XOR': xor}[op_str]
    return reduce(op, array)
