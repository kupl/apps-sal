def growing_plant(upSpeed, downSpeed, desiredHeight):
    result = 0
    height = 0
    while(True):
        result += 1
        height += upSpeed
        if height >= desiredHeight:
            break
        height -= downSpeed
    return result
