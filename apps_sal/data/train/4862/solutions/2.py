def put_the_cat_on_the_table(pos, c):
    if not (0 <= pos[0] < len(c) and 0 <= pos[1] < len(c[0])):
        return 'NoCat'
    find_one = next(([i, j.index(1)] for (i, j) in enumerate(c) if 1 in j), None)
    if not find_one:
        return 'NoTable'
    f = ('D' if pos[0] < find_one[0] else 'U') * abs(pos[0] - find_one[0])
    s = ('R' if pos[1] < find_one[1] else 'L') * abs(pos[1] - find_one[1])
    return f + s
