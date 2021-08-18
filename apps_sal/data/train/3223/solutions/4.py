
import math


def find_closest_value(x):
    if x < 4:
        return 4

    n = math.sqrt(x / 130)
    n_low = math.floor(n)
    seed = 130 * n_low**2
    n_inc = n_low * 65
    candidates = [seed,
                  seed + 4 + 1 * n_inc,
                  seed + 13 + 2 * n_inc,
                  seed + 69 + 3 * n_inc,
                  seed + 130 + 4 * n_inc]
    candidates = sorted(candidates, reverse=True)
    candidates = sorted(candidates, key=lambda a: abs(a - x))
    return candidates[0]
