def put_the_cat_on_the_table(cat, room):
    ((cy, cx), h, w) = (cat, len(room), len(room[0]))
    if not (0 <= cy < h and 0 <= cx < w):
        return 'NoCat'
    (ty, tx) = next(((y, x) for y in range(h) for x in range(w) if room[y][x]), (-1, -1))
    if ty < 0:
        return 'NoTable'
    (ver, dy) = ('U' if ty < cy else 'D', abs(ty - cy))
    (hor, dx) = ('L' if tx < cx else 'R', abs(tx - cx))
    return f'{hor * dx}{ver * dy}'
