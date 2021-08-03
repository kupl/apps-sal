def triangle(row):
    l = len(row)
    for i in range(l - 1):
        new_row = ""
        for v, v1 in zip(row, row[1:]):
            if v == v1:
                new_row += v
            else:
                new_row += list({'R', 'G', 'B'} - {v, v1})[0]
        row = new_row
    return row
