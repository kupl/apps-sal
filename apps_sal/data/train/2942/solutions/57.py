import math
def fold_to(distance):
    if distance < 0:
        return None
    fold = math.ceil(math.log(distance/0.0001, 2)) if distance else 0
    return fold if fold > 0 else 0

