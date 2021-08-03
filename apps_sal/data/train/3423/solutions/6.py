from itertools import combinations


def solve(arr, n):
    for i in range(1, len(arr) + 1):
        for j in combinations(arr, i):
            if sum(j) % n == 0:
                return True
    return False
