from itertools import zip_longest, starmap
from statistics import mean
from operator import eq

def vector_affinity(a, b):
    return not (a or b) or mean(starmap(eq, zip_longest(a, b, fillvalue='¯\_(ツ)_/¯')))
