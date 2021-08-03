def growing_plant(upSpeed, downSpeed, desiredHeight):
    cnt = 1
    for i in range(upSpeed, desiredHeight, upSpeed - downSpeed):
        cnt += 1
    return cnt
