def min_dot(a, b):
    (a, b) = (sorted(a), sorted(b, reverse=True))
    return sum((x * y for (x, y) in zip(a, b)))
