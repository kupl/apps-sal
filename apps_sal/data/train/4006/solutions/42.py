import operator
from functools import reduce


def basic_op(operator_mark, value1, value2):
    d = {'+': operator.add,
         '-': operator.sub,
         '*': operator.mul,
         '/': operator.truediv}
    return d[operator_mark](value1, value2)
