def growing_plant(upSpeed, downSpeed, desiredHeight):
    return max(0, (desiredHeight - downSpeed - 1) // (upSpeed - downSpeed)) + 1
