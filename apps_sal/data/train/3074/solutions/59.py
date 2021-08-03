def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 0

    for i in range(1, 10000):
        days += 1
        height += upSpeed
        print(f'After day {i}: {height}')

        if height >= desiredHeight:
            break

        height -= downSpeed
        print(f'After night {i}: {height}')

        if height >= desiredHeight:
            break

    return days
