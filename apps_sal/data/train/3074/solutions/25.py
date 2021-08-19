def growing_plant(up_speed, down_speed, desired_height):
    count = 1
    height = up_speed
    while height < desired_height:
        height -= down_speed
        height += up_speed
        count += 1
    return count
