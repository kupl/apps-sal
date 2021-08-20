def distance(p1, p2):
    if len(p1) != len(p2) or len(p1) < 1:
        return -1
    return sum(((p1[i] - p2[i]) ** 2 for i in range(len(p1)))) ** 0.5
