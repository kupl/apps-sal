import math


def distance(p1, p2):
    if p1 == [] or p2 == [] or len(p1) != len(p2):
        return -1
    diff = []
    for i in range(len(p1)):
        diff.append((p1[i] - p2[i]) ** 2)
    return math.sqrt(sum(diff))
