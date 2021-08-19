from math import ceil, floor


def will_it_balance(stick, terrain):
    c = sum((i * m for (i, m) in enumerate(stick, 1))) / sum(stick)
    (a, b) = (floor(c), ceil(c))
    return all((x or not a <= i <= b for (i, x) in enumerate(terrain, 1)))
