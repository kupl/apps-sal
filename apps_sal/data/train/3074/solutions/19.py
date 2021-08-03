import math


def growing_plant(upSpeed, downSpeed, desiredHeight):
    oneDay = upSpeed - downSpeed

    if desiredHeight - oneDay <= 0 or desiredHeight <= upSpeed:
        return 1

    sum = 0
    count = 0

    while desiredHeight - downSpeed > sum:
        sum += oneDay
        count += 1

    return count
