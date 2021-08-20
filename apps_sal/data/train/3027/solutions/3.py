def is_solved(board):
    return sum(board, []) == list(range(0, len(board) ** 2))
