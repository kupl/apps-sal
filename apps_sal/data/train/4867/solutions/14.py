def chess_board_cell_color(cell1, cell2):
    return True if (ord(cell1[0]) - ord(cell2[0])) % 2 == (ord(cell1[1]) - ord(cell2[1])) % 2 else False
