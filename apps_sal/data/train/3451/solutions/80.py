def triangle(row):
    if len(row) == 1:
        return row
    colors = {'GB': 'R', 'BG': 'R', 'GG': 'G', 'RR': 'R', 'BB': 'B', 'RB': 'G', 'BR': 'G', 'RG': 'B', 'GR': 'B'}
    zipped = list(zip(row, row[1:]))
    row = ''
    for x in zipped:
        row += colors[''.join(x)]
    return triangle(row)
