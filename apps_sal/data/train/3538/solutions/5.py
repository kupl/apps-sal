def sinus(u):
    y = (abs(u) * 16 - 8) * u
    return (abs(y) * 0.224 + 0.776) * y


def scroller(t, a, p):
    return '\n'.join((' ' * round((sinus(i % p / p - 1 / 2) + 1) * a) + c for (i, c) in enumerate(t)))
