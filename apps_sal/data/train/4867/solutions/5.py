black = lambda cell: (cell[0] in {'A', 'C', 'E', 'G'}) ^ int(cell[1])%2
chess_board_cell_color = lambda a, b : black(a)==black(b)
