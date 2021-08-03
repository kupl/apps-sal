def connect_four_place(columns):
    player, board, placed = 1, [['-'] * 7 for _ in range(6)], [-1] * 7
    for c in columns:
        player ^= 1
        board[placed[c]][c] = "YR"[player]
        placed[c] -= 1
    return board
