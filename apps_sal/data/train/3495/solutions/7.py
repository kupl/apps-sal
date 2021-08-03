from collections import Counter


def solve(a, b):
    aa = Counter(a)
    bb = Counter(b)

    for k, v in list(bb.items()):
        diff = aa[k] - v
        aa[k] -= v
        if diff < 0:
            return 0

    return sum(aa.values())
