def growing_plant(upSpeed, downSpeed, desiredHeight):
    count=0
    a=0
    if desiredHeight==0:
        return 1
    while not a>=desiredHeight:
        a+=upSpeed
        if a<desiredHeight:
            a-=downSpeed
        count+=1
    return count
