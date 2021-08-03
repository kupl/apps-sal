def chess_board(r, c): return [["OX"[(i + j) % 2] for j in range(c)] for i in range(r)]
