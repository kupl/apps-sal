from functools import reduce
import operator


def logical_calc(array, op):
    if op == "AND":
        o = operator.and_
    elif op == "OR":
        o = operator.or_
    elif op == "XOR":
        o = operator.xor

    return reduce(o, array)
