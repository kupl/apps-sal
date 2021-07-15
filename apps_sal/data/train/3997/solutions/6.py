from itertools import permutations, filterfalse

def solve(s, k):
    return len(list(filterfalse(lambda x: int(''.join(x))%k, permutations(s.split(), 2))))
