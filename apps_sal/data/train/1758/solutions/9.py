from itertools import permutations as pm
permutations=lambda s: map(''.join, set(pm(s)))
