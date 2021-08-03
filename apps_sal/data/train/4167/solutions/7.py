from functools import reduce
from operator import mul


def descriptions(arr):
    r = []
    seq = 0
    for x, y in zip(arr[:-1], arr[1:]):
        if y - x == 1:
            seq += 1
        else:
            if seq > 0:
                r.append(seq + 1)
                seq = 0
    if seq > 0:
        r.append(seq + 1)
    return reduce(mul, [2**(x - 1) for x in r]) if r else 1
