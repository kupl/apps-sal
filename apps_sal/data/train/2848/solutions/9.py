from itertools import combinations_with_replacement as comb


def find(arr, n):
    return sum(sum(c) == n for i in range(1, len(arr) + 1) for c in comb(arr, i))
