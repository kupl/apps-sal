import math


def count_paths(N, coords):
    t = N - 1 - coords[1] + coords[0]
    if t == 0:
        return 0

    return math.factorial(t) // (math.factorial(coords[0]) * math.factorial(t - coords[0]))
