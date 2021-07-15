def put_the_cat_on_the_table(cat, room):
    if not (0 <= cat[0] < len(room) and 0 <= cat[1] < len(room[0])):
        return 'NoCat'
    aim = None
    for row, rows in enumerate(room):
        for col, place in enumerate(rows):
            if place == 1:
                aim = (row, col)
                break
    if not  aim:
        return 'NoTable'
    else:
        route = cat[0] - aim[0], cat[1] - aim[1]
    if cat == aim:
        return ''
    else:
        return ('U' * route[0] if route[0] >= 0 else 'D' * abs(route[0])) + (
            'L' * route[1] if route[1] >= 0 else 'R' * abs(route[1]))
