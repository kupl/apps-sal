def squares_needed(grains):
    (s, r) = (0, 0)
    while grains > r:
        s += 1
        r += 2 ** (s - 1)
    return s
