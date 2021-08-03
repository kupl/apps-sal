def triangle(row):
    row = list(row)
    while len(row) > 1:
        row = [l if l == r else list(set('RGB') - set(l + r))[0] for l, r in zip(row, row[1:])]
    return row[0]
