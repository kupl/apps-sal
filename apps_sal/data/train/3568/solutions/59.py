def bumps(road):
    x = road.count('n')
    if x <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'
