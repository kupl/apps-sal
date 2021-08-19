def chess_board(r, c):
    return [['OX'[i + j & 1] for i in range(c)] for j in range(r)]
