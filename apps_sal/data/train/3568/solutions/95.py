def bumps(road):
    n_count = road.count('n')
    if n_count > 15:
        return 'Car Dead'
    elif n_count <= 15:
        return 'Woohoo!'
    return
