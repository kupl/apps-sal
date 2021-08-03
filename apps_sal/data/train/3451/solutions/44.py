def triangle(row):
    dir = {'BG': 'R', 'RG': 'B', 'BR': 'G', 'GB': 'R', 'GR': 'B', 'RB': 'G', 'BG': 'R'}
    for _ in range(len(row) - 1):
        row = tuple(dir.get(f'{row[i]}{row[i+1]}', row[i]) for i in range(len(row) - 1))
    return row[0]
