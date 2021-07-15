def covered_pawns(pawns):
    board = [[0]*8 for _ in range(8)]
    for c,r in pawns:
        board[8 - int(r)][ord(c) - 97] = 1
    return sum(board[i][j] and (j and board[i+1][j-1] or 7-j and board[i+1][j+1]) for i in range(7) for j in range(8))
