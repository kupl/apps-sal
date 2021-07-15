def triangle(row):
    MAP = {'RR': 'R', 'GG': 'G', 'BB': 'B', 'RG': 'B', 'RB': 'G', 'GR': 'B', 'GB': 'R', 'BR': 'G', 'BG': 'R'}
    while len(row) > 1:
        row = ''.join([MAP[''.join(x)] for x in zip(row, row[1:])])
    return row
