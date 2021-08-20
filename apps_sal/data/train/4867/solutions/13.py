def chess_board_cell_color(cell1, cell2):
    (r1, c1) = cell1
    (r2, c2) = cell2
    return abs(ord(r1) - ord(r2)) % 2 == (int(c1) - int(c2)) % 2
