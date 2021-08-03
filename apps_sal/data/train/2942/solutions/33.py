import math


def fold_to(distance):
    return (math.ceil(math.log2(distance / 0.0001)) if distance >= 0.0001 else None if distance < 0 else 0)
