import math


def predict_age(*ages):
    return math.sqrt(sum((i * i for i in ages))) // 2
