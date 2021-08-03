import math


def sum_circles(*args):
    return 'We have this much circle: ' + str(int(round(sum((i * i * math.pi / 4) for i in args), 0)))
