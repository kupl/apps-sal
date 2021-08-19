def distance_between_points(a, b):
    return sum((x * x for x in [a.x - b.x, a.y - b.y, a.z - b.z])) ** 0.5
