from itertools import permutations
def closest_sum(s, n): return min([sum(i) for i in permutations(s, 3)], key=lambda x: abs(x - n))
