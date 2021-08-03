import math


def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed >= desiredHeight:
        return 1
    else:
        return math.ceil((desiredHeight - downSpeed) / (upSpeed - downSpeed))
