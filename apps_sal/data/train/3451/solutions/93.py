def triangle(row):
    MAP = {'RR': 'R', 'GG': 'G', 'BB': 'B', 'RG': 'B', 'RB': 'G', 'GR': 'B', 'GB': 'R', 'BR': 'G', 'BG': 'R'}
    while len(row) > 1:
        row = [MAP[row[i] + row[i + 1]] for i in range(len(row) - 1)]
    return row[0]
