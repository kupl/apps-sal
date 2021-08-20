from itertools import permutations


def solve(stg, k):
    return sum((1 for (m, n) in permutations(stg.split(), 2) if int(f'{m}{n}') % k == 0))
