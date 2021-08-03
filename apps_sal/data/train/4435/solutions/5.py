from collections import Counter
from functools import reduce
from math import gcd


def has_subpattern(string):
    prev, *counts = set(Counter(string).values())
    if prev == 1 and not counts:
        return False

    for c in counts:
        prev = gcd(prev, c)
        if prev == 1:
            return False
    return True
