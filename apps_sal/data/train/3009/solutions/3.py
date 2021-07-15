pairs = lambda a: sum(abs(b - a) == 1 for a, b in zip(*[iter(a)]*2))
