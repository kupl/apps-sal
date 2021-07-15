from math import pi

def sum_circles(*args):
    return "We have this much circle: %.0f" % sum([(d/2.0)**2 * pi for d in args])
