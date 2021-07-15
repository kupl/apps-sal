def bumps(road):
    bumps = [x for x in road if x == 'n']
    if len(bumps) > 15:
        return 'Car Dead'
    return 'Woohoo!'
