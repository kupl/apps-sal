def triangle(row):
    colors = {'RR': 'R', 'GG': 'G', 'BB': 'B', 'RG': 'B', 'GR': 'B', 'GB': 'R', 'BG': 'R', 'RB': 'G', 'BR': 'G'}
    while not len(row) == 1:
        row = ''.join((colors[row[i] + row[i + 1]] for i in range(len(row) - 1)))
    return row
