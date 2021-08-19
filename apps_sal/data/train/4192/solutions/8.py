from itertools import combinations


def pairwise(arr, n):
    (r, c) = (0, [])
    for ((i, a), (j, b)) in combinations(enumerate(arr), 2):
        if a + b == n and i not in c and (j not in c):
            r += i + j
            c.extend([i, j])
    return r
