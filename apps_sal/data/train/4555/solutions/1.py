from functools import reduce
from operator import mul


def string_color(name):
    if len(name) > 1:
        xs = list(map(ord, name))
        r = sum(xs) % 256
        g = reduce(mul, xs) % 256
        b = abs(xs[0] - sum(xs[1:])) % 256
        return f"{r:02X}{g:02X}{b:02X}"
