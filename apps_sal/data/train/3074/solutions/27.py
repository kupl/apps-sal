def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed >= desiredHeight:
        return 1
    return int(1 + (desiredHeight - upSpeed) / (upSpeed - downSpeed) + bool((desiredHeight - upSpeed) % (upSpeed - downSpeed)))
