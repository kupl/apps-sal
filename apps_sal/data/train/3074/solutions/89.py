def growing_plant(upSpeed, downSpeed, desiredHeight):
    dia = 0
    height = 0
    while True:
        height = height + upSpeed
        dia += 1
        if height >= desiredHeight:
            return dia
        height = height - downSpeed
