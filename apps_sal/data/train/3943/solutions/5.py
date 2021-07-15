import math
def ellipse(a, b):
    perimeter = round(math.pi*(3/2*(a+b) - math.sqrt(a*b)), 1)
    area = round(math.pi*a*b, 1)
    return f'Area: {area}, perimeter: {perimeter}'
