def growing_plant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight-upSpeed <=0:
        return 1
    return 1+ growing_plant(upSpeed, downSpeed, desiredHeight-upSpeed+downSpeed)
