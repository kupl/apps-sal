def fortune(f0, p, c0, n, i):
    for t in range(n - 1):
        f0 = int(f0 + f0 * p / 100 - c0)
        c0 = int(c0 + c0 * i / 100)
    if f0 >= 0:
        return True
    return False
