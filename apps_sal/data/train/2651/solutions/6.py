prod2sum = lambda a, b, c, d: sorted(map(list, {tuple(sorted(map(abs, s))) for s in ((a*c - b*d, a*d + b*c), (a*d - b*c, a*c + b*d))}))
