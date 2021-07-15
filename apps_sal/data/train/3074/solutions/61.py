def growing_plant(upSpeed, downSpeed, desiredHeight):
    d=0
    e=0
    if desiredHeight<upSpeed:
        return 1
    else:
        while d<desiredHeight:
            d+=upSpeed
            e+=1
            if d>=desiredHeight:
                return e
            else:
                d-=downSpeed
        return e
