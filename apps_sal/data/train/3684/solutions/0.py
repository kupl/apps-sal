def is_orthogonal(u, v):
    return sum((i * j for (i, j) in zip(u, v))) == 0
