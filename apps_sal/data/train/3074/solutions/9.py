def growing_plant(upSpeed, downSpeed, desiredHeight):
    if (desiredHeight <= upSpeed):
        return 1
    days = int(desiredHeight / upSpeed)
    desiredHeight -= days * (upSpeed - downSpeed)
    return days + growing_plant(upSpeed, downSpeed, desiredHeight)
