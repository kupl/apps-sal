import math


def ModularInverse(a, b):
    coeffs = []
    while b > 0:
        coeffs.append(math.floor(a / b))
        a, b = b, a % b
    c1 = 1
    c2 = 0
    for co in coeffs[::-1]:
        c1, c2 = c2, c1 - co * c2
    return c2


def collatz_steps(n, steps):
    a = 1
    b = 0
    m = 1
    for i in range(len(steps)):
        m = m * 2
        if steps[i] == 'U':
            a = a * 3
            b = 3 * b + 2**i
    x = ((-b) * ModularInverse(m, a)) % m + m * math.floor(n / m)
    if (x < n):
        x = x + m
    return x
