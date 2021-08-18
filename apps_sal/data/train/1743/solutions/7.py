import math


def collatz_steps(n, steps):
    a = 1
    b = 0
    m = 1
    for i in range(len(steps)):
        m = m * 2
        if steps[i] == 'U':
            a = a * 3
            b = 3 * b + 2**i
    b = m - (b % m)
    a = a % m
    coeffs = []
    ae = m
    be = a
    while be > 0:
        coeffs.append(math.floor(ae / be))
        ae, be = be, ae % be
    xe = 0
    ye = 1
    for co in coeffs[::-1]:
        xe, ye = ye - co * xe, xe
    ai = xe % m
    x = (b * ai) % m
    x = x + m * math.floor(n / m)
    if (x < n):
        x = x + m
    return x
