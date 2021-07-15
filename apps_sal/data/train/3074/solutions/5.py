def growing_plant(upSpeed, downSpeed, desiredHeight):
    return max((desiredHeight - upSpeed - 1) // (upSpeed - downSpeed) + 1, 0) + 1
