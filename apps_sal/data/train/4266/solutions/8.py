def min_dot(a, b):
    a = sorted(a)
    b = sorted(b)[::-1]
    return sum([x * y for (x, y) in zip(a, b)])
