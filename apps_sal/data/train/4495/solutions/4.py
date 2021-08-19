FUNCS = dict(zip('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split(), (12.0.__eq__, 95.0.__lt__, 34.0.__eq__, 0.0.__eq__, lambda n: not n % 2, 56.0.__eq__, lambda n: abs(n) == 666)))


def am_I_afraid(day, n):
    return FUNCS[day](n)
