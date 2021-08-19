from operator import add, sub, truediv, mul


def basic_op(operator, v1, v2):
    op = {'+': add, '-': sub, '*': mul, '/': truediv}
    return op[operator](v1, v2)
