def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = upSpeed
    counter = 1
    if height >= desiredHeight:
        return counter
    else:
        while height < desiredHeight:
            height += upSpeed - downSpeed
            counter += 1
        return counter
