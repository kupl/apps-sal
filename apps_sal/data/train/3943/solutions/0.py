from math import pi


def ellipse(a, b):
    return f'Area: {pi * a * b:.1f}, perimeter: {pi * (1.5 * (a + b) - (a * b) ** 0.5):.1f}'
