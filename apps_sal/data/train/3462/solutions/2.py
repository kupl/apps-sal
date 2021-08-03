from functools import reduce
from operator import or_, xor


def disjunction(operands, is_exclusive):
    return reduce(xor if is_exclusive else or_, operands)
