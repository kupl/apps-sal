from itertools import permutations

def solve(s,k):
    return sum(not v%k for v in map(int, map(''.join, permutations(s.split(),2))))
