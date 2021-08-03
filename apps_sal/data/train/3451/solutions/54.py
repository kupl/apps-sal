def triangle(row):
    if len(row) == 1:
        return row
    r = ''
    for i in range(1, len(row)):
        if row[i] == row[i - 1]:
            r += row[i]
        else:
            l = ['R', 'G', 'B']
            l.remove(row[i])
            l.remove(row[i - 1])
            r += l[0]
    return triangle(r)
