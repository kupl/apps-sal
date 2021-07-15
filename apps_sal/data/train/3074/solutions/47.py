def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    n = 0
    while height < desiredHeight:
        height += upSpeed
        n += 1
        if height < desiredHeight:
            height -= downSpeed
        else:
            break
    return n if upSpeed < desiredHeight else 1
