import math


def sum_circles(*args):
    t = round(sum([math.pi * d ** 2 / 4 for d in args]))
    return 'We have this much circle: {}'.format(int(t))
