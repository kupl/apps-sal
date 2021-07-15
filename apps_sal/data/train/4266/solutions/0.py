def min_dot(a, b):
    return sum(x * y for (x, y) in zip(sorted(a), sorted(b, reverse = True)))
