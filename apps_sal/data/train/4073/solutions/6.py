def crossing_sum(m, r, c): return sum(m[r]) + sum(l[c] for i, l in enumerate(m) if i != r)
