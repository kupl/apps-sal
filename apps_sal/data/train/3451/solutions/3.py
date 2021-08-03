comb = {'GG': 'G', 'BR': 'G', 'RB': 'G', 'RR': 'R', 'BG': 'R', 'GB': 'R', 'BB': 'B', 'RG': 'B', 'GR': 'B'}


def triangle(row):
    if len(row) == 1:
        return row
    return (triangle(''.join(comb[row[i:i + 2]] for i in range(len(row) - 1))))
