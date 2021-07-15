from math import pi

def sum_circles(*rs):
    total = int(round(sum(pi * r**2 / 4 for r in rs)))
    return 'We have this much circle: {}'.format(total)
