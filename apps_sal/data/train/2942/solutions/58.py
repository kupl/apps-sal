import math


def fold_to(distance):
    if distance < 0:
        return None
    if distance < 0.0001:
        return 0
    else:
        return math.ceil(math.log(distance / 0.0001) / math.log(2))
