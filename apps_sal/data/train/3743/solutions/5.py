def chess_board(a, b):
    return [list("OXXO"[i % 2::2] * (b // 2 + 1))[:b] for i in range(a)]
