def is_solved(board):
    return all(a == b for a, b in enumerate(bx for by in board for bx in by))
