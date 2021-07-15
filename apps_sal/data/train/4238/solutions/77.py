import math
def squares_needed(grains):
    if grains == 0:
        return 0
    if grains %2 == 0:
        needed  = (int(math.log2(grains)))+1
    elif grains == 1:
        return 1
    else:
        needed = (int(math.log2(grains-1)))+1


    return needed
