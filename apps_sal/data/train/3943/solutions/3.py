import math

def ellipse(a, b):
    '''Return area and approximated perimeter of an ellipse'''
    
    area = math.pi * a * b
    perimeter = math.pi * (1.5 * (a + b) - math.sqrt(a * b))
    return f'Area: {round(area, 1)}, perimeter: {round(perimeter, 1)}'
