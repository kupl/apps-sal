from itertools import combinations_with_replacement as comb


def find(arr, n):
    return sum(sum(L) == n for i in range(1, len(arr) + 1) for L in comb(arr, i))
