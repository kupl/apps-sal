def put_the_cat_on_the_table(cat, room):
    ty, tx = next(((i, j) for i, row in enumerate(room) for j, v in enumerate(row) if v == 1), ('No', 'Table'))
    cy, cx = cat
    if cy < 0 or cx < 0 or cy + 1 > len(room) or cx + 1 > len(room[0]):
        return 'NoCat'
    if ty + tx == 'NoTable':
        return ty + tx
    return ('U' if (ty - cy) < 0 else 'D') * (abs(ty - cy)) + ('L' if (tx - cx) < 0 else 'R') * (abs(tx - cx))
