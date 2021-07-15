def bumps(road):
    counter = 0
    for i in road:
        if i == 'n':
            counter += 1
            continue
    return 'Woohoo!' if counter <= 15 else 'Car Dead'

