from math import log2,ceil

def fold_to(distance):
    if distance < 0 : return None
    elif distance==0 : return 0
    return max(0,ceil(log2(distance*10000)))
