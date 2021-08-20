def bumps(road):
    sum = 0
    for i in road:
        if i is 'n':
            sum += 1
        if sum > 15:
            return 'Car Dead'
    return 'Woohoo!'
