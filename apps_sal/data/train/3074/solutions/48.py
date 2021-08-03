def growing_plant(upSpeed, downSpeed, desiredHeight):
    for i in range(1, 1000):
        if i * (upSpeed - downSpeed) >= desiredHeight or (i - 1) * (upSpeed - downSpeed) + upSpeed >= desiredHeight:
            return i
