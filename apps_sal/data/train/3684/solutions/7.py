is_orthogonal = lambda u, v: not sum(a * b for a, b in zip(u, v))
