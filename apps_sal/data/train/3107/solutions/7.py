import math


def distance(p1, p2):
    if len(p1) != len(p2) or len(p1) == 0:
        return -1
    if len(p1) == 1:
        return math.fabs(p1[0] - p2[0])
    dist = 0
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
    return dist ** 0.5
