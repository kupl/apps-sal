def put_the_cat_on_the_table(cat, room):
    nr, nc = len(room), len(room[0])
    cr, cc = cat
    if not (cr in range(nr) and cc in range(nc)):
        return 'NoCat'
    try:
        tr, tc = next((r, c) for r in range(nr) for c in range(nc) if room[r][c])
    except StopIteration:
        return 'NoTable'
    dr, dc = tr - cr, tc - cc
    return 'D' * dr + 'U' * -dr + 'R' * dc + 'L' * -dc
