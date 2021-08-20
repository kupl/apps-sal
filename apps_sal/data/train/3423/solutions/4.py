from itertools import combinations


def solve(x, n):

    def combs(x):
        return [c for i in range(1, len(x) + 1) for c in combinations(x, i)]
    return any(map(lambda x: sum(x) % n == 0, combs(x)))
