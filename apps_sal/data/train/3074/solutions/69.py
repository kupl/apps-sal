def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    noite = 0
    dias = 0
    while desiredHeight > height and desiredHeight > noite:
        height += upSpeed
        noite = height
        height -= downSpeed
        dias += 1
    return dias
