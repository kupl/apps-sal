# https://www.johndcook.com/blog/2015/10/06/number-of-digits-in-n/
from scipy.special import gammaln
from math import log, floor


def count(n):
    return floor(gammaln(n + 1) / log(10.0)) + 1
