def my_crib(n):
    mult = 2 * n - 1
    top_roof = '_' * (n * 2 + 1)
    top_roof = top_roof.center(n * 6 + 1, ' ')
    resulty = ''
    resulty += top_roof + '\n'
    for i in range(n * 2):
        medium_roof = '/' + '_' * int(2 * (i + n) + 1) + '\\'
        medium_roof = medium_roof.center(n * 6 + 1, ' ')
        resulty += medium_roof + '\n'
    for j in range(n - 1):
        top_house = '|' + ' ' * (n * 6 - 1) + '|'
        resulty += top_house + '\n'
    upper_door = '|' + ' ' * (n * 2) + '_' * mult + ' ' * (n * 2) + '|'
    resulty += upper_door + '\n'
    for h in range(n - 1):
        medium_house = '|' + ' ' * mult + '|' + ' ' * mult + '|' + ' ' * mult + '|'
        resulty += medium_house + '\n'
    basement = '|' + '_' * mult + '|' + '_' * mult + '|' + '_' * mult + '|'
    resulty += basement
    return resulty
