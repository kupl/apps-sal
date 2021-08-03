colors = {'R', 'G', 'B'}


def pair(v):
    dif = colors.difference(v)
    return v[0] if len(dif) == 2 else dif.pop()


def triangle(row):
    if len(row) == 1:
        return row[0]
    next_row = []
    for i in range(len(row) - 1):
        next_row.append(pair(row[i:i + 2]))
    return triangle(next_row)
