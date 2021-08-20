conv = {'RR': 'R', 'GG': 'G', 'BB': 'B', 'RG': 'B', 'GR': 'B', 'RB': 'G', 'BR': 'G', 'BG': 'R', 'GB': 'R'}


def triangle(row):

    def dec(row):
        return ''.join((conv[row[x:x + 2]] for x in range(len(row) - 1)))
    while len(row) - 1:
        row = dec(row)
    return row
