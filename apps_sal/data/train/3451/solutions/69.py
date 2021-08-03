def triangle(row):
    next_row = row
    for i in range(len(row)):
        row = next_row
        next_row = []
        for j in range(len(row) - 1):
            next_row.append(clr_add(row[j], row[j + 1]))
    return row[0]


def clr_add(a, b):
    if a is b:
        return a
    if (a is 'R' and b is 'G') or (a is 'G' and b is 'R'):
        return 'B'
    if (a is 'G' and b is 'B') or (a is 'B' and b is 'G'):
        return 'R'
    if (a is 'B' and b is 'R') or (a is 'R' and b is 'B'):
        return 'G'
