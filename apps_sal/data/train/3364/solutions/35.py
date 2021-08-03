import math


def predict_age(a1, a2, a3, a4, a5, a6, a7, a8):
    l = [a1 ** 2, a2 ** 2, a3 ** 2, a4 ** 2, a5 ** 2, a6 ** 2, a7 ** 2, a8 ** 2]
    return int(math.sqrt(sum(l)) / 2)
