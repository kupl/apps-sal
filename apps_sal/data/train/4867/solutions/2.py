def chess_board_cell_color(cell1, cell2):
    is_black = lambda c: (c[0] in "BDFH") ^ (c[1] in "1357")
    return is_black(cell1) == is_black(cell2)
