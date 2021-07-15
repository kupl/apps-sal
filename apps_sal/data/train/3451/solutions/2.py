def triangle(row):
    while len(row) > 1:
        row = ''.join(({'R', 'G', 'B'} - {a, b}).pop() if a != b else a for a, b in zip(row, row[1:]))
    return row
