def chess_board(rows, columns):
    return [['OX'[(row + column) % 2] for column in range(columns)] for row in range(rows)]
