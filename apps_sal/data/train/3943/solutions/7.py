import math
def ellipse(a, b):
    s = str(round(math.pi * a * b, 1))
    l = str(round(math.pi * (3 / 2 * (a + b) - math.sqrt(a * b)), 1))
    return "Area: "+s+", perimeter: "+l
