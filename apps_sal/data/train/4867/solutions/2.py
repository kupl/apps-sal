def chess_board_cell_color(cell1, cell2):
    def is_black(c): return (c[0] in "BDFH") ^ (c[1] in "1357")
    return is_black(cell1) == is_black(cell2)
