import math


def coordinates(p1, p2, d=0):
    formula = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    distance = round(formula, d)
    return distance
