from operator import and_
from operator import or_
from operator import xor
from functools import reduce


def logical_calc(array, op):
    if op == 'XOR':
        return reduce(xor, array)
    elif op == 'AND':
        return reduce(and_, array)
    elif op == 'OR':
        return reduce(or_, array)
