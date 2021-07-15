def put_the_cat_on_the_table(cat, room):
    if not (0 <= cat[0] < len(room) and 0 <= cat[1] < len(room[0])):
        return 'NoCat'
    t = ([(y, x) for y, row in enumerate(room) for x, col in enumerate(row) if col == 1] + [None])[0]
    if not t:
        return 'NoTable'
    h = 'L' * abs(t[1] - cat[1]) if t[1] - cat[1] < 0 else 'R' * (t[1] - cat[1])
    return h + ('U' * abs(t[0] - cat[0]) if t[0] - cat[0] < 0 else 'D' * (t[0] - cat[0]))
