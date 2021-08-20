def is_orthogonal(u, v):
    return not sum((a * b for (a, b) in zip(u, v)))
