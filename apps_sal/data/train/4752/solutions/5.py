from collections import Counter
from functools import reduce


def gcd(a, b):
    return gcd(b, a % b) if b else a


def has_subpattern(s):
    return (lambda r: (lambda g: ''.join((k * (v // g) for (k, v) in sorted(r.items()))))(reduce(gcd, r.values())))(Counter(s))
