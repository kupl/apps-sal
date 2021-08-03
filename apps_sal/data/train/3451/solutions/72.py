def triangle(row):
    place, y = 0, ''
    while len(row) > 1:
        place, y = 0, ''
        while place < len(row) - 1:
            if row[place] == row[place + 1]:
                y += row[place]
            if row[place] == 'R' and row[place + 1] == 'B':
                y += 'G'
            if row[place] == 'B' and row[place + 1] == 'R':
                y += 'G'
            if row[place] == 'R' and row[place + 1] == 'G':
                y += 'B'
            if row[place] == 'G' and row[place + 1] == 'R':
                y += 'B'
            if row[place] == 'G' and row[place + 1] == 'B':
                y += 'R'
            if row[place] == 'B' and row[place + 1] == 'G':
                y += 'R'
            place += 1
        row = y
    return row
