def triangle(row):
    if len(row) == 1:
        return row
    new = ""
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            new += row[i]
        else:
            if row[i] == 'R' and row[i+1] == 'G':
                new += 'B'
            elif row[i] == 'G' and row[i+1] == 'R':
                new += 'B'
            elif row[i] == 'G' and row[i+1] == 'B':
                new += 'R'
            elif row[i] == 'B' and row[i+1] == 'G':
                new += 'R'
            elif row[i] == 'R' and row[i+1] == 'B':
                new += 'G'
            elif row[i] == 'B' and row[i+1] == 'R':
                new += 'G'
    return triangle(new)
