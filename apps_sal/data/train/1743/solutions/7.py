import math


def collatz_steps(n, steps):
    # ax = b mod m
    # a = 3 ^ (# of U in steps)
    # b = -f(#steps-1) where
    #   f(-1) = 0
    #   f(i)=3f(i-1)+2^i when steps[i]==U
    #   f(i)=f(i-1)      when steps[i]==D
    # m = 2 ^ (#steps)
    a = 1
    b = 0
    m = 1
    for i in range(len(steps)):
        m = m * 2
        if steps[i] == 'U':
            a = a * 3
            b = 3 * b + 2**i
    b = m - (b % m)
    # ax = b mod m
    a = a % m
    #  x = ba^-1 mod m
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
    # x = ba^-1 + mC
    x = x + m * math.floor(n / m)
    if (x < n):
        x = x + m
    return x
