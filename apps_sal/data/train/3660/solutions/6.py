from math import factorial as f
def bino(x, y): return f(x) // f(y) // f(x - y)


def count_paths(N, coords):
    d1, d2 = N - coords[1] - 1, coords[0]
    return bino(d1 + d2, min(d1, d2)) if d1 + d2 else 0
