def is_solved(board):
    board = sum(board, [])
    return board == sorted(board)
