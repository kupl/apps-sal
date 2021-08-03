from re import compile
from functools import reduce
from operator import add, sub, mul, floordiv as div, pow, mod

REGEX = compile(r"^\d+|[^\d]\d+").findall
D = {'+': add, '-': sub, '*': mul, '/': div, '^': pow, '%': mod}


def no_order(equation):
    L = REGEX(equation.replace(" ", ""))
    try:
        return reduce(lambda x, y: D[y[0]](x, int(y[1:])), L[1:], int(L[0]))
    except:
        return None
