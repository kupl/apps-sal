def bumps(road):
    list(road)
    bump_counter = 0
    for bump in road:
        if bump == 'n':
            bump_counter += 1
    if bump_counter <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
