from math import sqrt, floor


def predict_age(a1, a2, a3, a4, a5, a6, a7, a8):
    ages = [a1, a2, a3, a4, a5, a6, a7, a8]
    return floor(sqrt(sum([x * x for x in ages])) / 2)
