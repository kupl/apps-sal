def closest_sum(a, n): return min(map(sum, __import__('itertools').combinations(a, 3)), key=lambda c: abs(c - n))
