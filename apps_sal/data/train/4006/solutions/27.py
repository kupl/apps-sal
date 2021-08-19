import operator as op


def basic_op(operator, value1, value2):
    return {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}[operator](value1, value2)
