from collections import Counter
from math import factorial as fact
from functools import reduce
from operator import mul


def perms(element):
    s = str(element)
    c = Counter(s)
    return fact(len(s)) / reduce(mul, [fact(n) for n in c.values()], 1)
