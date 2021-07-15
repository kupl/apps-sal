def tv_remote(word):
    display = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
               ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
               ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
               ['p', 'q', 'r', 's', 't', '.', '@', '0'],
               ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    rows = [0]
    columns = [0]
    for letter in word:
        for row in display:
            if letter in row:
                rows.append(display.index(row))
                for cell in row:
                    if letter == cell:
                        columns.append(row.index(letter))
    moves = 0
    for n in range(1, len(rows)):
        moves += abs(rows[n] - rows[n - 1])
    for n in range(1, len(columns)):
        moves += abs(columns[n] - columns[n - 1])
    return moves + len(word)
