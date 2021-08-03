def solve(p):
    d2 = -1
    for d in range(1, int(p ** 0.5) + 1):
        if (p - 1) % d == 0:
            k = pow(10, d, p)
            if k == 1:
                return f'{d}-sum'
            elif k == p - 1:
                return f'{d}-altsum'
            t = (p - 1) // d
            k = pow(10, t, p)
            if k == 1 or k == p - 1:
                d2 = t
    return f'{d2}-sum' if pow(10, d2, p) == 1 else f'{d2}-altsum'
