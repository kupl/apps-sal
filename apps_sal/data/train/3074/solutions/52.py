from math import ceil

def growing_plant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight < upSpeed:
        return 1
    return ceil((desiredHeight - downSpeed) / (upSpeed - downSpeed))
