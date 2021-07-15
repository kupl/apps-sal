def growing_plant(upSpeed, downSpeed, desiredHeight):
    i=1
    height=0
    while(True):
        height=height+upSpeed
        if height>=desiredHeight:
            break
        else:
            height=height-downSpeed
        i=i+1
    return i
