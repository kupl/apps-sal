from operator import and_, xor, or_
from functools import reduce


def logical_calc(array, op):
    operations = {"AND": and_, "OR": or_, "XOR": xor}

    return reduce(operations[op], array)
