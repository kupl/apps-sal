def triangle(row):
    if len(row) == 1:
        return row[0]

    colors = set(["B", "G", "R"])
    newrow = []
    for (l, r) in zip(row, row[1:]):
        if l == r:
            newrow.append(l)
        else:
            newrow.extend(colors - set([l, r]))

    return triangle(newrow)
