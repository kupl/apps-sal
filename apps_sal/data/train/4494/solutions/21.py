def points(c): return sum(3 * (h > g) + (h == g)for h, _, g in c)
