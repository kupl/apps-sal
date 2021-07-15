sel_number = lambda n, d: sum(1 for a in map(str, xrange(n+1)) if len(set(a)) == len(a) > 1 and all(int(b) - int(a) <= d and b > a for a, b in zip(a[:-1], a[1:])))
