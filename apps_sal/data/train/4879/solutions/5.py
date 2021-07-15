from collections import Counter
from itertools import chain
from operator import mul
from math import factorial

def count_perms(matrix):
    n = len(matrix) * len(matrix[0])
    c = Counter(chain.from_iterable(matrix))
    return factorial(n) / reduce(mul, map(factorial, c.itervalues()))
