import math
def area_of_polygon_inside_circle(r, n):
    return round(0.5 * r * r * n * math.sin(2 * math.pi / n), 3)
