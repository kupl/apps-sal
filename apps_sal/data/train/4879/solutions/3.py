from collections import Counter
from functools import reduce
from math import factorial
from operator import mul


def count_perms(matrix):
    return factorial(len(matrix) * len(matrix[0])) // reduce(mul, map(factorial, Counter(sum(matrix, [])).values()))
