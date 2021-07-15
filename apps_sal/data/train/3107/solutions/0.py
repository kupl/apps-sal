def distance(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5 if len(p1) == len(p2) > 0 else -1
