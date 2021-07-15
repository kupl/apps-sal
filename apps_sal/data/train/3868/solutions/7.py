from itertools import permutations;closest_sum=lambda s,n:min([sum(i) for i in permutations(s, 3)], key=lambda x: abs(x - n))
