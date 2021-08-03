def solve(s, k): return sum(int(x + y) % k == 0for x, y in __import__('itertools').permutations(s.split(), 2))
