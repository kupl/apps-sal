def chess_board(rows, columns):
    return [['OX'[(row + col) % 2] for col in range(columns)] for row in range(rows)]
