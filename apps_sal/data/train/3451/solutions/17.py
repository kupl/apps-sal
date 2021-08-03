def triangle(row):
    while len(row) > 1:
        s = ''
        for a, b in zip(row, row[1:]):
            if a == b:
                s += a
            else:
                s += (set('RGB') ^ set(a + b)).pop()
            row = s
    return row
