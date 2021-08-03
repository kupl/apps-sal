from math import factorial


def count_paths(N, coords):
    if N == 1:
        return 0
    x = coords[0]
    y = N - 1 - coords[1]
    return factorial(x + y) // (factorial(x) * factorial(y))
