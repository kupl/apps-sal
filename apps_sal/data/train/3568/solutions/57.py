def bumps(road):
    result = 0
    for i in road:
        if i == 'n':
            result += 1
    if result <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'
