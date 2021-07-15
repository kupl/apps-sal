from collections import Counter
from math import factorial
import operator

def ssc_forperm(xs):
    n = len(xs)
    p = factorial(n) // reduce(operator.mul,
        map(factorial, Counter(xs).itervalues()))
    sxs = sorted(xs)
    return [
        {"total perm": p},
        {"total ssc": (n + 1) * p * sum(xs) // 2},
        {"max ssc": sum(i * x for (i, x) in enumerate(sxs, 1))},
        {"min ssc": sum(i * x for (i, x) in enumerate(reversed(sxs), 1))}]
