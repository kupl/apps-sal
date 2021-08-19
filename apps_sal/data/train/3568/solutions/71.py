def bumps(road):
    bump = 15
    for char in road:
        if char == 'n':
            bump = bump - 1
    return 'Car Dead' if bump < 0 else 'Woohoo!'
