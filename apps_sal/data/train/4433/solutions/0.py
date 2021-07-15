import operator
from functools import reduce

OPS = {
    "AND": operator.and_,
    "OR" : operator.or_,
    "XOR": operator.xor
}

def logical_calc(array, op):
    return reduce(OPS[op], array)

