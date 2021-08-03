def between(x, y): return [x] if x == y else [x] + between(x + 1, y)
