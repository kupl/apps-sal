def chess_board_cell_color(cell1, cell2):
    return sum(map(ord, cell1)) % 2 == sum(map(ord, cell2)) % 2
