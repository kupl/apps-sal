def growing_plant(upSpeed, downSpeed, desiredHeight):
    x = upSpeed
    output = 1
    while x < desiredHeight:
        x += upSpeed
        x -= downSpeed
        output += 1
    return output
