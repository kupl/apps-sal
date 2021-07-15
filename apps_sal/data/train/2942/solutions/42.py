import math
def fold_to(distance):
    thickness = 0.0001
    if distance == 0: 
        return 0
    elif distance > 0:
        return max(math.ceil(math.log(distance,2)-math.log(thickness,2)),0)
    else:
        return None
