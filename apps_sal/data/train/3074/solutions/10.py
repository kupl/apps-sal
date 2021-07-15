def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    day = 1
    num_days = 0
    while height < desiredHeight:
      if day == True: 
        height += upSpeed
        day = 0
        num_days += 1
      else:
        height -= downSpeed
        day = 1
    return num_days
