mix = {('G', 'G'): 'G', ('G', 'R'): 'B', ('G', 'B'): 'R', ('B', 'G'): 'R', ('B', 'R'): 'G', ('B', 'B'): 'B', ('R', 'G'): 'B', ('R', 'R'): 'R', ('R', 'B'): 'G'}


def triangle(row):
    if len(row) == 1:
        return row
    r = ''
    for c in range(len(row) - 1):
        r += mix.get((row[c], row[c + 1]), '')
    return triangle(r)
