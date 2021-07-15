import math
def predict_age(*ages):
    return int(math.sqrt(sum([num*num for num in ages])) / 2)
