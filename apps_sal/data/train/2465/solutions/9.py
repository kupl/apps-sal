class Solution:

    def divisorGame(self, N: int) -> bool:
        return recurse_game(N, 0)


def find_factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors


lookup = {}


def recurse_game(N, P):
    if (N, P) in lookup:
        return lookup[N, P]
    if N <= 1 and P == 0:
        lookup[N, P] = False
        return False
    elif N <= 1 and P == 1:
        lookup[N, P] = True
        return True
    next_P = 0 if P == 1 else 1
    results = []
    for factor in find_factors(N):
        results.append(recurse_game(N - factor, next_P))
    if P == 0:
        if True in results:
            lookup[N, P] = True
            return True
        else:
            lookup[N, P] = False
            return False
    if P == 1:
        if False in results:
            lookup[N, P] = False
            return False
        else:
            lookup[N, P] = True
            return True
