def is_solved(board):
    return sum(board, []) == list(range(len(board)**2))
