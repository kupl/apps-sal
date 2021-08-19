def black(cell):
    return (cell[0] in {'A', 'C', 'E', 'G'}) ^ int(cell[1]) % 2


def chess_board_cell_color(a, b):
    return black(a) == black(b)
