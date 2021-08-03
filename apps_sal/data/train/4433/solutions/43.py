import operator
from functools import reduce


def logical_calc(array, op):
    return reduce(getattr(operator, '__{}__'.format(op.lower())), array)
