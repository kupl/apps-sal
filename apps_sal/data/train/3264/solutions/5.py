from scipy.special import gammaln
from math import log, floor


def count(n):
    return floor(gammaln(n + 1) / log(10.0)) + 1
