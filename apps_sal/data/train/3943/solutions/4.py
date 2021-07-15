def ellipse(a, b):
    import math
    area = math.pi * a * b
    p = math.pi * (1.5 * (a + b) - math.sqrt(a * b))
    return "Area: " + str(round(area, 1)) + ", perimeter: " + str(round(p, 1))
