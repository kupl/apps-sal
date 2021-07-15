def growing_plant(upSpeed, downSpeed, desiredHeight):

    growth = upSpeed
    counter = 1

    while growth < desiredHeight:
        growth += upSpeed - downSpeed
        counter += 1
    
    return counter
