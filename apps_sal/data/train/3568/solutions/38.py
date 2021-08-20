def bumps(road):
    count = 0
    for char in road:
        if char == 'n':
            count += 1
    if count > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
