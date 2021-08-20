from math import *


def scroller(t, a, p):
    return '\n'.join((' ' * round(a + a * sin(i / p * tau)) + c for (i, c) in enumerate(t)))
