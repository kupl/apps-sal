def is_orthogonal(u, v):
    return sum(a*b for a, b in zip(u, v)) == 0
