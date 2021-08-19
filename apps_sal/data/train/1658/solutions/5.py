from collections import defaultdict
from fractions import Fraction
from itertools import count

# memoization, just in case
POWER = defaultdict(list)
F = [1]


def fact(x):
    while len(F) <= x:
        F.append(F[-1] * len(F))
    return F[x]


def expand(x, digit):
    # Change the floats into a fraction
    if type(x) == float:
        a, b = str(x).split('.')
        l = 10**(len(b))
        x = Fraction(int(a) * l + int(b), l)
    # Init
    res, mini = Fraction(0), 10**(digit - 1)
    if not x in POWER:
        POWER[x].append(1)
    # Core of the function
    for i in count():
        res += Fraction(POWER[x][i], fact(i))
        if mini <= res.numerator:
            return [res.numerator, res.denominator]
        if len(POWER[x]) <= i + 1:
            POWER[x].append(POWER[x][-1] * x)
