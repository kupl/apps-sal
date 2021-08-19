from itertools import combinations


def help67(arr):
    S = set(arr)
    for (a, b) in combinations(arr, 2):
        if 2 * b - a in S:
            yield (a, b, 2 * b - a)


def solve(arr):
    c = 0
    for i in help67(arr):
        c += 1
    return c
