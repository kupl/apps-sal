from math import log10
from operator import itemgetter


def find_longest(arr):
    return max(list(zip((int(log10(a)) for a in arr), arr)), key=itemgetter(0))[1]
