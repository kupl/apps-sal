import math


def heron(*liste):
    sum = 0
    for i in liste:
        sum += i
    s = sum / 2
    return round(math.sqrt(s * (s - liste[0]) * (s - liste[1]) * (s - liste[2])), 2)
