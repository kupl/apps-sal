import math


def fold_to(distance):
    return math.ceil(math.log(distance / 0.0001, 2)) if distance > 0.0001 else None if distance < 0 else 0
