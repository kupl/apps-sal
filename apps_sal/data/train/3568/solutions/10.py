def bumps(road):
    
    track = 0
    
    for el in road:
        if el == 'n':
            track += 1
    
    if track > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
