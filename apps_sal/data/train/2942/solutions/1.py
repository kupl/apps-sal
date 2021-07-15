import math
def fold_to(d):
    if d<0:
        return None
    if d<0.0001:
        return 0
    return math.ceil(math.log(d/0.0001,2))
