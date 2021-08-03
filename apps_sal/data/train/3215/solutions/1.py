def reduce_pyramid(base):
    c, t, ll = 1, 0, len(base) - 1
    for i, v in enumerate(base):
        t += c * v
        c = c * (ll - i) // (i + 1)
    return t
