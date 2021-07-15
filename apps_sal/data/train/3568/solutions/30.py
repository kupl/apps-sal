def bumps(road):
    counter = 0
    for i in road:
        if i == 'n':
            counter += 1
    if counter > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
