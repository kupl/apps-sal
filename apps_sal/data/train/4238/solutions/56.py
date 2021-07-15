import math
def squares_needed(grains):
    if grains==0:
        return 0
    else:
        x=math.log(grains)//math.log(2)+1
        return x

