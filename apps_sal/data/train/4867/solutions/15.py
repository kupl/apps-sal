def chess_board_cell_color(cell1, cell2):
    return int(cell1, 35) % 2 == int(cell2, 35) % 2
