def growing_plant(upSpeed, downSpeed, desiredHeight):
    desiredHeight -= upSpeed
    return max(1, -(-desiredHeight // (upSpeed - downSpeed)) + 1)
