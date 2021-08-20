import math


def ellipse(a, b):
    area = str(round(a * b * math.pi, 1))
    perimetro = str(round(math.pi * (3 / 2 * (a + b) - math.sqrt(a * b)), 1))
    return 'Area: ' + area + ', perimeter: ' + perimetro
