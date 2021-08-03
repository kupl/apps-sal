from itertools import permutations as pm
def permutations(s): return map(''.join, set(pm(s)))
