from itertools import combinations_with_replacement as comb


def find(lst, n):
    return sum((1 for l in range(1, len(lst) + 1) for c in comb(lst, l) if sum(c) == n))
