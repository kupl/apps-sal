from itertools import permutations as p


def solve(s, k):
    return len([j for j in [int(''.join(i)) for i in p(s.split(), 2)] if j % k == 0])
