def growing_plant(upSpeed, downSpeed, desiredHeight):
    desiredHeight -= upSpeed
    if desiredHeight<0: desiredHeight = 0
    return -(-desiredHeight//(upSpeed-downSpeed)) + 1
