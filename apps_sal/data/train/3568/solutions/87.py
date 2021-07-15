def bumps(road):
    n = [x for x in road if x == 'n'].count('n')
    return 'Woohoo!' if n <= 15 else 'Car Dead'
