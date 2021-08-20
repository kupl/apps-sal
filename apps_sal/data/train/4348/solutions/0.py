t = ((800, 'lava'), (120, 'blaze rod'), (80, 'coal'), (15, 'wood'), (1, 'stick'))


def calc_fuel(n):
    (s, r) = (n * 11, {})
    for (d, e) in t:
        (r[e], s) = divmod(s, d)
    return r
