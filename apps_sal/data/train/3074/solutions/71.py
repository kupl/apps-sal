import math


def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 0
    while True:
        height += upSpeed
        days += 0.5
        if height >= desiredHeight:
            break
        height -= downSpeed
        days += 0.5
    return math.ceil(days)
