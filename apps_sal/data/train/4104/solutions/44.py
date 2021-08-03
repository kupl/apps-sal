from itertools import combinations


def max_tri_sum(n):
    l = set(n)
    return max([x + y + z for x, y, z in list(combinations(l, 3))])
