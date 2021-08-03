from math import *


def fold_to(d):
    if d < 0:
        return None
    elif floor(d * 10000) == 0:
        return 0
    else:
        return ceil(log(d * 10000, 2))
