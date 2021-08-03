COLS = {
    ('G', 'G'): 'G',
    ('B', 'B'): 'B',
    ('R', 'R'): 'R',
    ('G', 'B'): 'R',
    ('G', 'R'): 'B',
    ('R', 'B'): 'G',
    ('R', 'G'): 'B',
    ('B', 'R'): 'G',
    ('B', 'G'): 'R'
}


def triangle(row):
    while (len(row) > 1):
        row = [COLS[x, y] for x, y in zip(row[:-1], row[1:])]
    return row[0]
