from operator import __and__, __or__, __xor__
from functools import reduce


def logical_calc(a, op):
    if op == "AND":
        return reduce(__and__, a)
    if op == "OR":
        return reduce(__or__, a)
    else:
        return reduce(__xor__, a)
