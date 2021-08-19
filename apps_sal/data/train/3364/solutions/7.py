import math


def predict_age(*ages):
    return int(math.sqrt(sum((age * age for age in ages))) / 2)
