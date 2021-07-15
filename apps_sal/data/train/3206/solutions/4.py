from math import pi
def sum_circles(*args):
    return 'We have this much circle: {}'.format(int(round(sum(pi*(d/2.0)**2 for d in args))))
