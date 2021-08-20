from itertools import permutations


def solve(s, k):
    return sum((int(a + b) % k == 0 for (a, b) in permutations(s.split(), 2)))
