from math import pi

def ellipse(p, q):
    return f'Area: {round(pi * q * p, 1)}, perimeter: {round(pi * (3/2*(p+q) - (p*q) ** .5), 1)}'
