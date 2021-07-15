def is_solved(board):
    flat = [y for x in board for y in x]
    return flat == sorted(flat)
