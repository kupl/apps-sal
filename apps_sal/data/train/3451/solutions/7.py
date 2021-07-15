def triangle(row):
    color = {'GG': 'G', 'BB': 'B', 'RR': 'R', 'BG': 'R', 'GR': 'B', 'BR': 'G', 'GB': 'R', 'RG': 'B', 'RB': 'G'}
    return triangle("".join(color.get(l+row[j+1]) for j, l in enumerate(row[:-1]))) if len(row) > 1 else row
