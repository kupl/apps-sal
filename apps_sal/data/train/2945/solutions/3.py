def fortune(f0, p, c0, n, i):
    f = f0
    c = c0

    for year in range(n - 1):
        f = int(f + f * (p / 100)) - int(c)
        c = int(c + c * (i / 100))

    return f >= 0
