def growing_plant(upSpeed, downSpeed, desiredHeight):
    if (upSpeed >= desiredHeight) or (desiredHeight == 0):
        return 1
    res = int((desiredHeight - upSpeed) / (upSpeed - downSpeed))
    if (desiredHeight - upSpeed) % (upSpeed - downSpeed) > 0:
        res += 1
    return res + 1

