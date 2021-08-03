def distance_between_points(a, b):
    return (sum((getattr(a, i) - getattr(b, i))**2 for i in 'xyz'))**0.5
