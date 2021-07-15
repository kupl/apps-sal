from bisect import bisect
from itertools import accumulate


def save(sizes, hd): 
    return bisect(list(accumulate(sizes)), hd)
