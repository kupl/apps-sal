def bumps(road):

    commute = road

    bumps = commute.count('n')

    condition_1 = bumps < 16
    condition_2 = bumps >= 16

    if condition_1:
        return 'Woohoo!'
    if condition_2:
        return 'Car Dead'
