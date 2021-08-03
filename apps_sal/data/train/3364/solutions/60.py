from math import sqrt


def predict_age(*ages):
    a = [pow(x, 2) for x in ages]
    a = sum(a)
    a = sqrt(a)
    a = a // 2
    return a
