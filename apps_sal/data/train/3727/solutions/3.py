from itertools import combinations
from math import hypot

limit = 10000000
candidates = ((a,b,hypot(a,b)) for a,b in combinations(range(1, 1000), 2))
D = {a*b*int(c):[a,b,int(c)] for a,b,c in candidates if c.is_integer() and a*b*c < limit}
pythagorean_triplet = D.__getitem__
