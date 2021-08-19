def reduce_pyramid(base):
    (n, c, r) = (len(base) - 1, 1, 0)
    for (i, x) in enumerate(base):
        r += c * x
        c = c * (n - i) // (i + 1)
    return r
