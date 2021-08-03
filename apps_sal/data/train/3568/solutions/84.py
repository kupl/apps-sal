def bumps(road):
    x = road.count('n', 0)
    if x <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'
