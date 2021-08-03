def area_of_polygon_inside_circle(r, n):
    import math
    a = (360 / (2 * n)) * (0.017453292519943295)
    b = 2 * r * math.sin(a)
    c = r * math.cos(a)
    return round((1 / 2) * (b) * (c) * (n), 3)
