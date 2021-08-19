import math


def predict_age(*args):
    return math.sqrt(sum((x * x for x in args))) // 2
