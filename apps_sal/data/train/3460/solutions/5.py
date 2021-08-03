from collections import Counter
from functools import reduce
from math import factorial
from operator import mul


def uniq_count(string):
    return factorial(len(string)) // reduce(mul, map(factorial, Counter(string.lower()).values()), 1)
