def distance_between_points(a, b):
    return sum((getattr(a, attr) - getattr(b, attr)) ** 2 for attr in "xyz") ** 0.5
