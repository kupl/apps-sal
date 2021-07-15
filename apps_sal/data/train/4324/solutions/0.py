def display_board(board, width):
    board = [c.center(3) for c in board]
    rows = ["|".join(board[n:n+width]) for n in range(0, len(board), width)]
    return ("\n" + "-"*(4*width - 1) + "\n").join(rows)
