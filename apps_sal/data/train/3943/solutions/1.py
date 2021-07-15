from math import pi

def ellipse(a, b):
    perimeter = pi * (3/2*(a+b) - (a*b)**0.5)
    area = pi * a*b
    return f'Area: {area:.1f}, perimeter: {perimeter:.1f}'
