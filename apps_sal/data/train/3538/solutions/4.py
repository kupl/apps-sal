from math import *


def scroller(s, a, l):
    return '\n'.join(('{:>{:.0f}}'.format(c, 1 + a * (1 + sin(n * 2 * pi / l))) for (n, c) in enumerate(s)))
