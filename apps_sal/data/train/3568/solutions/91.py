def bumps(road):
    b = 0
    for i in road:
        if i == 'n':
            b += 1
    return 'Woohoo!' if b <= 15 else 'Car Dead'
