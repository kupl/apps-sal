def solve(s, k):
    return sum((int(x + y) % k == 0 for (x, y) in __import__('itertools').permutations(s.split(), 2)))
