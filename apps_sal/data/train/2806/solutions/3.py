def whose_turn(positions):
    (wk1, wk2, bk1, bk2) = positions.split(';')
    cciw = cell_color_is_white
    return not cciw(wk1) ^ cciw(wk2) ^ cciw(bk1) ^ cciw(bk2)


def cell_color_is_white(cell):
    return (ord(cell[0]) + ord(cell[1])) % 2 == 1
