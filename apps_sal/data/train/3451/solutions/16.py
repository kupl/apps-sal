def triangle(row):
    while len(row) > 1:
        row = [a if a == b else (set('RGB') ^ {a, b}).pop() for a, b in zip(row, row[1:])]
    return row[0]
