from operator import mul
from math import factorial
from functools import reduce
from collections import Counter


def perms(inp):
    return factorial(len(str(inp))) // reduce(mul, map(factorial, Counter(str(inp)).values()), 1)
