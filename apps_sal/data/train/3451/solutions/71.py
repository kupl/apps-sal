colors = 'RGB'


def triangle(row):
    if len(row) <= 1:
        return row
    if len(row) == 2:
        if row[0] == row[1]:
            return row[0]
        else:
            return colors.replace(row[0], '').replace(row[1], '')
    return triangle(''.join(list(map(triangle, [row[i:i + 2] for i in range(len(row) - 1)]))))
