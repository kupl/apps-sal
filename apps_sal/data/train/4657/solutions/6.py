from itertools import permutations


def sort_by_perfsq(arr):
    def isSquare(n): return int(n**0.5) == n**0.5
    return sorted(arr, key=lambda n: (sum(isSquare(int(''.join(nS))) for nS in set(permutations(str(n)))), -n), reverse=True)
