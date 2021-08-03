import re
from operator import add, sub, floordiv, mul, pow, mod

OPS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv,
    '^': pow,
    '%': mod,
}


def no_order(equation):
    equation = equation.replace(' ', '')
    if not equation:
        return None
    it = iter(re.findall(r'\d+|\D+', equation))
    x = int(next(it))
    for op, y in zip(it, it):
        try:
            x = OPS[op](x, int(y))
        except ZeroDivisionError:
            return None
    return x
