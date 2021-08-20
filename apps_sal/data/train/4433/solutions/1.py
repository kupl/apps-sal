from operator import and_, or_, xor
from functools import reduce
OPERATOR = {'AND': and_, 'OR': or_, 'XOR': xor}


def logical_calc(array, op):
    return reduce(OPERATOR[op], array)
