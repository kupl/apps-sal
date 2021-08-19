def bumps(road):
    b = road.count('n')
    if b > 15:
        s = 'Car Dead'
    else:
        s = 'Woohoo!'
    return s
