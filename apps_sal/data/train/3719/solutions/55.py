x = (9.45 - 10.67) / (1.52 - 1.83)
a = 9.45 - 1.52 * x


def starting_mark(h):
    return round(a + x * h, 2)
