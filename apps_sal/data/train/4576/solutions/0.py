from fractions import gcd
from itertools import product, starmap
from statistics import mean

def gcd_matrix(a, b):
    return round(mean(starmap(gcd, product(a, b))), 3)
