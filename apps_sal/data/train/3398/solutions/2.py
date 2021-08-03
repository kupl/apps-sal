solve = lambda a, d={-1, 0, 1}: min((sum(l)for l in ([abs(a[0] + u + (a[1] + v - a[0] - u) * n - x)for n, x in enumerate(a)]for u in d for v in d)if set(l) <= d), default=-1)
