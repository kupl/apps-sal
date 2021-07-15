def growing_plant(upSpeed, downSpeed, desiredHeight):
    return max(1,int(0.99+ (desiredHeight-downSpeed)/(upSpeed-downSpeed)))
