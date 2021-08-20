import itertools


def int_diff(arr, n):
    count = 0
    for (i, j) in itertools.combinations(arr, 2):
        if abs(i - j) == n:
            count += 1
    return count
