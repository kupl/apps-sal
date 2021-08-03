import math

PREFIXES = ['m', 'km', 'Mm', 'Gm', 'Tm', 'Pm', 'Em', 'Zm', 'Ym']


def meters(x):
    e = int(math.log(x, 1000))
    return '{0:g}{1}'.format(x / 1000.0**e, PREFIXES[e])
