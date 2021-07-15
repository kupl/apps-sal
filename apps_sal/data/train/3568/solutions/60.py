def bumps(road):
    a = 0
    for char in road:
        if str(char) == 'n':
            a += 1
    if a <= 15:
        return 'Woohoo!'
    if a > 15:
        return 'Car Dead'
