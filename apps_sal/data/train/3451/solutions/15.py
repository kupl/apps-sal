def triangle(row):
    while len(row) > 1:
        row = [[({*'RGB'} - {a, b}).pop(), a][a == b] for a, b in zip(row, row[1:])]
    return row[0]
