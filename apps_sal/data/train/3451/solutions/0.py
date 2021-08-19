COLORS = set('RGB')


def triangle(row):
    while len(row) > 1:
        row = ''.join((a if a == b else (COLORS - {a, b}).pop() for (a, b) in zip(row, row[1:])))
    return row
