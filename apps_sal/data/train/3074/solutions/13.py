def growing_plant(upSpeed, downSpeed, desiredHeight):
    #your code here
    day = 1
    plant_height = 0
    while True:
        plant_height += upSpeed
        if plant_height >= desiredHeight:
            return day
        plant_height -= downSpeed
        day += 1
