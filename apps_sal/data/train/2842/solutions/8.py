def coordinates(p1, p2, prec=0):
    return round(((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5, prec)
