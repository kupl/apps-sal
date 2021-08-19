import math


def fold_to(distance):
    if distance < 0:
        return None
    elif distance < 0.0001:
        return 0
    else:
        n = math.log(distance / 0.0001, 10) / math.log(2, 10) + 1
        return math.floor(n)
