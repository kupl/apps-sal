from operator import add, sub, mul, truediv
OPS = {'+': add, '-': sub, '*': mul, '/': truediv}


def basic_op(op, a, b):
    return OPS[op](a, b)
