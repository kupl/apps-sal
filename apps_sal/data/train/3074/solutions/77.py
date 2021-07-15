def growing_plant(upSpeed, downSpeed, desiredHeight):
    daily_growth = upSpeed - downSpeed
    if desiredHeight <= upSpeed:
        return 1
    elif (desiredHeight - upSpeed) % daily_growth == 0:
        return (desiredHeight - upSpeed) // daily_growth + 1
    else:
        return (desiredHeight - upSpeed) // daily_growth + 2

