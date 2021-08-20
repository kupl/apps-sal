import math


def predict_age(*args):
    res = 0
    for i in args:
        res += i * i
    return math.floor(math.sqrt(res) / 2)
