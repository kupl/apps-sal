import math


def fold_to(d):
    if d < 0:
        return None
    if d < .0001:
        return 0
    return math.ceil(math.log(10000 * d) / math.log(2))
