def histogram(a, n):
    r = [0] * (max(a, default=-1) // n + 1)
    for x in a:
        r[x // n] += 1
    return r
