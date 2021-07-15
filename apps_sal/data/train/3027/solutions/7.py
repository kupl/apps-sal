def is_solved(board):
    board2 = board[0] + board[1]
    board3 = board[0] + board[1]
    return sorted(board3) == board2
