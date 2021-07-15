import operator
from functools import reduce

def logical_calc(array, op):
    op = '__{}__'.format(op.lower())
    op = getattr(operator, op)
    return reduce(op, array)

