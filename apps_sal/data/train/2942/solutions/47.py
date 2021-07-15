from math import log2

def fold_to(distance):
    if distance < 0:
        return None
    elif distance == 0:
        return 0
    return max(int(log2(distance / 0.0001)) + 1, 0)
