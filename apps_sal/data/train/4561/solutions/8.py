solve = lambda s: all(abs(ord(x) - ord(y)) in (0, 2) for x, y in zip(s, s[::-1]))
