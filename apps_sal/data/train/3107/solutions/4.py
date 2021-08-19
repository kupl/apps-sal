def distance(p1, p2):
    return sum(((x - y) ** 2 for (x, y) in zip(p1, p2))) ** 0.5 if len(p1) == len(p2) > 0 else -1
