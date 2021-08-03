d = [
    (800, "lava"),
    (120, "blaze rod"),
    (80, "coal"),
    (15, "wood"),
    (1, "stick")
]


def calc_fuel(n):
    n *= 11
    r = {}
    for a, b in d:
        r[b] = n // a
        n %= a
    return r
