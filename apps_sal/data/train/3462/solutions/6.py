from operator import or_, xor
from functools import reduce


def disjunction(operands, is_exclusive):
    return reduce([or_, xor][is_exclusive], operands)
