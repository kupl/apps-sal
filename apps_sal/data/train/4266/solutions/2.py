def min_dot(a, b):
    return sum(map(int.__mul__, sorted(a), sorted(b)[::-1]))
