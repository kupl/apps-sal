import math


def growing_plant(upSpeed, downSpeed, desiredHeight):
    (days, height) = (0, 0)
    while True:
        days += 1
        height += upSpeed
        if height >= desiredHeight:
            return days
        height -= downSpeed
