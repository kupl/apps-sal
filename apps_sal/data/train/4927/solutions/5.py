from functools import reduce
from operator import xor
from scipy.misc import comb


def transform(A, x):
    return reduce(xor, map(lambda n: comb(n+1,x+1,exact=True),A))
