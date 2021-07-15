from math import sqrt

def factors(n):
    f = []
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            f.append([x, int(n / x)])
    return f

def sol_equa(n):
    ff = factors(n)
    res = []
    for f in ff:
        m = m = f[0] + f[1]
        n = f[1] - f[0]
        if (m % 2 == 0) and (n % 4 == 0):
            res.append([int(m / 2), int(n / 4)])
    return res
