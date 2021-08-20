from itertools import accumulate
from operator import add


def tram(stops, off, on):
    return max(accumulate((b - a for (a, b) in zip(off, on[:stops])), add))
