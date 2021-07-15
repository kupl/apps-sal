def min_dot(a, b):
    return sum((ai * bi) for ai, bi in zip(sorted(a), sorted(b, reverse=True)))
