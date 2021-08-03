def min_dot(a, b):
    return sum(i * j for i, j in zip(sorted(a), sorted(b)[::-1]))
