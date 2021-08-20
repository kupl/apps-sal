def put_the_cat_on_the_table(a, b):
    (cx, cy) = a
    if not (0 <= cx < len(b) and 0 <= cy < len(b[0])):
        return 'NoCat'
    if not any((any(x) for x in b)):
        return 'NoTable'
    (tx, ty) = next(((i, j) for (i, x) in enumerate(b) for (j, y) in enumerate(x) if y))
    return 'L' * (cy - ty) + 'R' * (ty - cy) + 'U' * (cx - tx) + 'D' * (tx - cx)
