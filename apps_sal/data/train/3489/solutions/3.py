from itertools import *


def save(sizes, hd):
    return sum((1 for _ in takewhile(hd.__ge__, accumulate(sizes))))
