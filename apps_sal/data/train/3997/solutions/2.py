from itertools import permutations

def solve(s,k):
    return sum(not int(a+b)%k for a,b in permutations(s.split(),2))
