from itertools import count


def compute_depth(n):
    res = set(map(str, range(10)))
    for a in count(1):
        res -= set(str(n * a))
        if not res:
            return a
