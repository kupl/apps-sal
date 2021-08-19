def triangle(row):
    k = 0
    while k < len(row):
        if row[k] == 'G' or row[k] == 'B' or row[k] == 'R':
            k += 1
            continue
        else:
            return print(' only R,G,B are allowed')
    if len(row) == 1:
        return row
    how_many = len(row) - 1
    lenght = len(row)
    new_row = ''
    i = 0
    j = 0
    while j < how_many:
        j = +1
        while True:
            if len(new_row) == len(row) - 1:
                if len(new_row) == 1:
                    return new_row
                row = new_row
                new_row = ''
                lenght = len(row)
                i = 0
                break
            if row[i] == row[i + 1]:
                new_row = new_row + row[i]
                i += 1
                continue
            elif row[i] == 'B' and row[i + 1] == 'G' or (row[i] == 'G' and row[i + 1] == 'B'):
                new_row = new_row + 'R'
                i += 1
                continue
            elif row[i] == 'R' and row[i + 1] == 'G' or (row[i] == 'G' and row[i + 1] == 'R'):
                new_row = new_row + 'B'
                i += 1
                continue
            elif row[i] == 'B' and row[i + 1] == 'R' or (row[i] == 'R' and row[i + 1] == 'B'):
                new_row = new_row + 'G'
                i += 1
                continue
            if len(new_row) == 1:
                return new_row
            else:
                row = new_row
                i = 0
