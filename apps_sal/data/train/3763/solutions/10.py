import operator
from functools import reduce

OPS = {
    "+": operator.__add__,
    "-": operator.__sub__,
    "*": operator.__mul__,
    "/": operator.__truediv__
}


def calculator(x, y, op):
    return reduce(OPS[op], (x, y)) if op in OPS and type(x) is type(y) is int else 'unknown value'
