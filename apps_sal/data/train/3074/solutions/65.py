def growing_plant(upSpeed, downSpeed, desiredHeight):
    actualGrowth_afterDay = upSpeed
    number_of_days = 1
    dailyGrowth = upSpeed - downSpeed
    while actualGrowth_afterDay < desiredHeight:
        number_of_days += 1
        actualGrowth_afterDay += dailyGrowth 
    return number_of_days
