import operator as op


def basic_op(operator, value1, value2):
    op_dict = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return op_dict[operator](value1, value2)
