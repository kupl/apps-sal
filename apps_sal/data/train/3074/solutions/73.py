def growing_plant(upSpeed, downSpeed, desiredHeight):
    return 1 + sum((upSpeed * d - downSpeed * (d - 1) < desiredHeight for d in range(1, 699)))
