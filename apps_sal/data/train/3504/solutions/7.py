def power_mod(b, e, m):
    (r, b) = (1, b % m)
    while e > 0:
        if e % 2 == 1:
            r = r * b % m
        (e, b) = (e >> 1, b * b % m)
    return r
