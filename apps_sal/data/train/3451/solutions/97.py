def new_row(row):
    combinations = ['BG', 'GB', 'RG', 'GR', 'BR', 'RB']
    res = ['R', 'R', 'B', 'B', 'G', 'G']
    row2 = ''
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row2 += row[i]
        else:
            row2 += res[combinations.index(row[i] + row[i + 1])]
    return row2
            

def triangle(row):
    if len(row) == 1:
        return row
    return triangle(new_row(row))
