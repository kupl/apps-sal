from collections import Counter
from itertools import permutations
from math import factorial
from operator import mul


def ssc(xs):
    return sum(i * x for i, x in enumerate(xs, 1))


def ssc_forperm(arr):
    m = reduce(mul, (factorial(x) for x in Counter(arr).values()))
    xs = [ssc(xs) for xs in permutations(arr)]
    return [{"total perm": len(xs) // m}, {"total ssc": sum(xs) // m}, {"max ssc": max(xs)}, {"min ssc": min(xs)}]
