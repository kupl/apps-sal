def triangle(row):
    while (len(row) > 1):
        temp = ""
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                col = row[i]
            else:
                col = ('RGB'.replace(row[i], '')).replace(row[i + 1], '')
            temp = temp + col
        row = temp
    return row
