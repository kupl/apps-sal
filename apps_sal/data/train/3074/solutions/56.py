import math


def growing_plant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight - upSpeed > 0:
        return 1 + math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed))
    return 1
