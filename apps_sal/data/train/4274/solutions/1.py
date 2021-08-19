from re import compile
from functools import reduce
from itertools import cycle, starmap
from operator import add, sub, mul, truediv as div, itemgetter
REGEX = compile('(\\d*)([a-z])(\\d*)').fullmatch


def extract(i, s):
    (a, b, c) = REGEX(s).groups()
    return (b, i, int(a + c))


def do_math(s):
    c = cycle((add, sub, mul, div))
    vals = sorted(starmap(extract, enumerate(s.split())))
    return round(reduce(lambda x, y: next(c)(x, y), map(itemgetter(2), vals)))
