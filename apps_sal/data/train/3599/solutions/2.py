from itertools import count
from string import digits


def f12(n, k):
    valid_digits = set(digits[:k])
    for x in count(n, n):
        s = str(x)
        if valid_digits.issuperset(s):
            return valid_digits.issubset(s)


def find_f1_eq_f2(n, k):
    return next(i for i in count(n + 1) if f12(i, k))
