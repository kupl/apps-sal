def triangle(row):
    str1 = ''
    i = len(row)
    while i > 1:
        for j in range(i - 1):
            if row[j] == row[j + 1]:
                str1 += row[j]
            elif row[j] != row[j + 1]:
                if row[j] == 'R' and row[j + 1] == 'G':
                    str1 += 'B'
                elif row[j] == 'R' and row[j + 1] == 'B':
                    str1 += 'G'
                elif row[j] == 'G' and row[j + 1] == 'B':
                    str1 += 'R'
                elif row[j] == 'G' and row[j + 1] == 'R':
                    str1 += 'B'
                elif row[j] == 'B' and row[j + 1] == 'R':
                    str1 += 'G'
                elif row[j] == 'B' and row[j + 1] == 'G':
                    str1 += 'R'
        row = str1
        str1 = ''
        i = len(row)
    return row
