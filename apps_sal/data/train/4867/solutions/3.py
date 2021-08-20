(b, chess_board_cell_color) = (lambda c: sum(map(ord, c)) & 1, lambda c, d: b(c) == b(d))
