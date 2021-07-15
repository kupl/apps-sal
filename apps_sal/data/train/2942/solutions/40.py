import math
def fold_to(distance):
    if distance < 0: return None
    su = 0.0001
    fold = 0
    while su < distance:
        su*=2
        fold+=1
    return fold
