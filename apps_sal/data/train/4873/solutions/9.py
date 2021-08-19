def distance_between_points(a, b):
    ss = [(a.__getattribute__(i) - b.__getattribute__(i)) ** 2 for i in 'xyz']
    return sum(ss) ** 0.5
