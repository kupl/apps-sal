def growing_plant(upSpeed, downSpeed, desiredHeight):
    (days, nights, height) = (0, 0, 0)
    if upSpeed >= desiredHeight:
        return 1
    else:
        while height <= desiredHeight:
            height += upSpeed
            days += 1
            if height >= desiredHeight:
                break
            height -= downSpeed
            nights += 1
        if nights > days:
            return nights
        else:
            return days
