def growing_plant(up_speed, down_speed, desired_height):
    current_height = 0
    days_gone = 0
    if up_speed >= 5 and up_speed <= 100 and (down_speed >= 2) and (down_speed < up_speed) and (desired_height >= 4) and (desired_height <= 1000):
        while True:
            days_gone += 1
            current_height += up_speed
            if current_height < desired_height:
                current_height -= down_speed
            else:
                return days_gone
                break
    else:
        return 1
