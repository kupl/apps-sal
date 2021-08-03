def growing_plant(upSpeed, downSpeed, desiredHeight):
    init_height = 0
    day_count = 0
    if init_height == desiredHeight:
        return 1
    else:
        while init_height < desiredHeight:
            init_height += upSpeed
            day_count += 1
            if init_height >= desiredHeight:
                print(init_height, day_count)
                return day_count
                break
            else:
                init_height -= downSpeed
                if init_height >= desiredHeight:
                    print(init_height, day_count)
                    return day_count
                    break
