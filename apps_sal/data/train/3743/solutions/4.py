def chess_board(rows, columns):
    board = []
    for row in range(rows):
        if row % 2:
            board.append(['X' if not column % 2 else 'O' for column in range(columns)])
        else:
            board.append(['O' if not column % 2 else 'X' for column in range(columns)])
    return board
