from operator import add, sub, mul, truediv


def basic_op(op, v, v2):
    return {'+': add, '-': sub, '*': mul, '/': truediv}[op](v, v2)
