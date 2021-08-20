def chess_board_cell_color(cell1, cell2):
    return sum((ord(c) + int(d) for (c, d) in (cell1, cell2))) % 2 == 0
