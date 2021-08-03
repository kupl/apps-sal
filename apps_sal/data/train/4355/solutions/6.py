from math import exp


def ex_euler(n):
    e = 0
    h = 1 / n
    y = 1 - h
    for i in range(1, n + 1):
        t = i / n
        e2 = exp(-2 * t)
        e4 = e2**2
        z = 1 + (e4 - e2) / 2
        e += abs(y - z) / z
        y += (2 - e4 - 2 * y) * h
    return e * 1000000 // (n + 1) / 1000000
