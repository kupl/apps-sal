from scipy.special import binom
from operator import xor
from functools import reduce


def transform(A, x):
    return reduce(xor, [int(round(binom(n + 1, x + 1))) for n in A])
