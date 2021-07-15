def growing_plant(upSpeed, downSpeed, desiredHeight):
    current_height = 0
    counter = 0
    if desiredHeight == 0:
        counter = 1
        return counter 
    else:
        while current_height < desiredHeight:
            current_height += upSpeed
            counter += 1
            if current_height >= desiredHeight:
                return counter
            else:
                current_height -= downSpeed

