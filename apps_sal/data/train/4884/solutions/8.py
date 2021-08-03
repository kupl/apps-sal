def connect_the_dots(paper):
    letters_input = [l for l in "abcdefghijklmnopqrstuvwxyz" if l in paper]
    table = [list(row) for row in paper.split("\n")[:-1:]]
    coordinates = [(row.index(letter), indx) for letter in letters_input for indx, row in enumerate(table) if letter in row]
    print(coordinates)
    for indx, coord in enumerate(coordinates[:-1:]):
        if coord[1] == coordinates[indx + 1][1]:
            for x in range(min(coord[0], coordinates[indx + 1][0]), max(coord[0], coordinates[indx + 1][0]) + 1):
                table[coord[1]][x] = "*"
        elif coord[0] == coordinates[indx + 1][0]:
            for y in range(min(coord[1], coordinates[indx + 1][1]), max(coord[1], coordinates[indx + 1][1]) + 1):
                table[y][coord[0]] = "*"
        else:
            step_x = (coordinates[indx + 1][0] - coord[0]) / abs(coord[0] - coordinates[indx + 1][0])
            lst_x = [int(coord[0] + step_x * k) for k in range(abs(coord[0] - coordinates[indx + 1][0]) + 1)]
            step_y = (coordinates[indx + 1][1] - coord[1]) / abs(coord[1] - coordinates[indx + 1][1])
            lst_y = [int(coord[1] + step_y * k) for k in range(abs(coord[1] - coordinates[indx + 1][1]) + 1)]
            for x, y in zip(lst_x, lst_y):
                table[y][x] = "*"
    res = "\n".join(["".join(row) for row in table]) + "\n"
    return res
