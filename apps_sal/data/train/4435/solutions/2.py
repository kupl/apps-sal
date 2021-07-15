from collections import Counter
from functools import reduce
import fractions


def gcd(*values):
    return reduce(fractions.gcd, values)


def has_subpattern(s):
    return gcd(*Counter(s).values()) != 1
