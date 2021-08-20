import numpy as np


def product(l):
    if not l:
        return None
    if 0 in l:
        return 0
    if len(l) == 1:
        return l[0]
    p = 1
    for i in l:
        p *= i
    return p
