def gcd(a, b):
    if a < b:
        b, a = a, b
    while b != 0:
        a, b = b, a % b
    return a


def mn_lcm(m, n):
    m, n = sorted([m, n])
    f = 1
    for i in range(m, n + 1):
        f = abs(i * f) // gcd(i, f)
    return f
