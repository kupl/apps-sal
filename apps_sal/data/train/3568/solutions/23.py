def bumps(road):
    k = list(road)
    count = 0
    for word in k:
        if word == 'n':
            count += 1
    if count < 16:
        return 'Woohoo!'
    else:
        return 'Car Dead'
