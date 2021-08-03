import itertools as it


def solve(s, k):
    return sum(n % k == 0 for n in map(int, map(''.join, it.permutations(s.split(), 2))))
