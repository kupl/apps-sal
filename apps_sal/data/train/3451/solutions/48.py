def triangle(row):
    while len(row) != 1:
        row2 = ''
        for i in range(len(row) - 1):
            if row[i] == row[i+1]:
                row2 += row[i]
            elif (row[i], row[i+1]) == ('R', 'B') or (row[i], row[i+1]) == ('B', 'R'):
                row2 += 'G'
            elif (row[i], row[i+1]) == ('R', 'G') or (row[i], row[i+1]) == ('G', 'R'):
                row2 += 'B'
            elif (row[i], row[i+1]) == ('G', 'B') or (row[i], row[i+1]) == ('B', 'G'):
                row2 += 'R'
        row = row2
    return row
