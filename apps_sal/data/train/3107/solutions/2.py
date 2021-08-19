def distance(p1, p2):
    if not (p1 or p2) or len(p1) != len(p2):
        return -1
    return sum(((y - x) ** 2 for (x, y) in zip(p1, p2))) ** 0.5
