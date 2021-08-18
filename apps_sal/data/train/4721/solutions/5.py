FUNCS = {
    'C': (lambda t: t, lambda t: t),
    'F': (lambda t: (t - 32) * 5 / 9, lambda t: t * 9 / 5 + 32),
    'K': (lambda t: t - 273.15, lambda t: t + 273.15),
    'R': (lambda t: (t - 491.67) * 5 / 9, lambda t: (t + 273.15) * 9 / 5),
    'De': (lambda t: 100 - t * 2 / 3, lambda t: (100 - t) * 3 / 2),
    'N': (lambda t: t * 100 / 33, lambda t: t * 33 / 100),
    'Re': (lambda t: t * 5 / 4, lambda t: t * 4 / 5),
    'Ro': (lambda t: (t - 7.5) * 40 / 21, lambda t: t * 21 / 40 + 7.5),
}


def convert_temp(t, org, to):
    return round(FUNCS[to][1](FUNCS[org][0](t)))
