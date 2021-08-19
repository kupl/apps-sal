def coordinates(p1, p2, p=0):
    return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5, p)
