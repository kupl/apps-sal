from operator import add, sub, mul, truediv, floordiv

div = truediv


def arithmetic(a, b, s): return eval(s[:3])(a, b)
