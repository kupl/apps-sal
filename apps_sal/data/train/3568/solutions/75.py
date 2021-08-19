def bumps(road):
    r = road
    c = r.count('n')
    if c < 16:
        return 'Woohoo!'
    else:
        return 'Car Dead'
