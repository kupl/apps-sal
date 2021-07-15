def bumps(road):
    counter = -1
    bumps = 0
    for x in road:
        counter += 1
        if road[counter] == 'n':
            bumps += 1
            print(bumps)
    if bumps <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'

