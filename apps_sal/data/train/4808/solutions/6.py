from itertools import product

def equalize(xs):
    return ['{:+d}'.format(x - xs[0]) for x in xs]
