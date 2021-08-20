def ellipse(a, b):
    import math
    area = math.pi * a * b
    perimeter = math.pi * (3 / 2 * (a + b) - math.sqrt(a * b))
    return 'Area: ' + str(round(area, 1)) + ', perimeter: ' + str(round(perimeter, 1))
