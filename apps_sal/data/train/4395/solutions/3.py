from math import log2


def next_higher(v):
    l = v & -v
    u = ~(v | l - 1) & -~(v | l - 1)
    return (v | u - 1) ^ u - 1 | u | (v & u - 1) >> int(log2(l)) + 1
