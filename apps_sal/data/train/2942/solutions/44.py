import math
def fold_to(distance):
    if distance<0:
        return None
    if distance < 0.0001:
        return 0
    return int(math.ceil(math.log(distance/0.0001,2)))
