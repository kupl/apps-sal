from collections import Counter


def solve(a):
    c = Counter((b > a) - (b < a) for a, b in zip(a, a[1:]))
    return 'R' * (len(c) - 1) + 'DA'[(max(c, key=c.__getitem__) + 1) // 2
                                     if len(c) == 1 or len(set(c.values())) != 1
                                     else a[0] > a[-1]]
