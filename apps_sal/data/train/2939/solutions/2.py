from itertools import combinations

s = {a**3 + b**3 for a, b in combinations(range(1, 1000), 2)}
s.discard(19**3 + 34**3)  # bug

def has_two_cube_sums(n):
    return n in s
