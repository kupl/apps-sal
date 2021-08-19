from itertools import groupby


def is_hollow(x):
    xs = [(key, sum((1 for _ in grp))) for (key, grp) in groupby(x)]
    mid = len(xs) // 2
    limit = len(xs) - (len(xs) > 1)
    return any((i == mid < limit for (i, (x, cnt)) in enumerate(xs) if x == 0 and cnt >= 3)) and sum((x == 0 for (x, _) in xs)) == 1
