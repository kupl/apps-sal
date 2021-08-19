def growing_plant(upSpeed, downSpeed, desiredHeight):
    (i, height) = (0, 0)
    while True:
        height += upSpeed
        i += 1
        if height >= desiredHeight:
            break
        height -= downSpeed
    return i
