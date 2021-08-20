from math import factorial as f


def count_paths(n, c):
    return f(c[0] + abs(n - c[1] - 1)) // (f(abs(n - c[1] - 1)) * f(c[0])) if n != 1 else 0
