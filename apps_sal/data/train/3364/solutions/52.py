import math


def predict_age(*args):
    return int(math.sqrt(sum((a * a for a in args))) / 2)
