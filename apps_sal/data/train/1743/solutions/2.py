def ModInv(a, m):
    return pow(a, (m >> 1) - 1, m)


def Ext_Euclid_Alg(a, m):
    (old_r, r) = (a, m)
    (old_s, s) = (1, 0)
    while r:
        q = old_r // r
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
    return old_s if old_s > 0 else old_s + m


def collatz_steps(n, steps):
    (a, b, m) = (1, 0, 1)
    for (i, s) in enumerate(steps):
        m *= 2
        if s == 'U':
            a *= 3
            b = 3 * b + 2 ** i
    x = -b * ModInv(a, m) % m
    x += m * (n // m)
    return x + m if x < n else x
