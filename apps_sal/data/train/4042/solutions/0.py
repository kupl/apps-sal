def points(R):
    from math import sqrt
    point = sum((int(sqrt(R * R - x * x)) for x in range(0, R + 1))) * 4 + 1
    return point
