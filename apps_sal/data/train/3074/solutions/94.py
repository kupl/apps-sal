def growing_plant(upSpeed, downSpeed, desiredHeight):
    #your code here
    up = upSpeed
    i = 1
    while up < desiredHeight :
        up += upSpeed
        up -= downSpeed
        i += 1
    return i
