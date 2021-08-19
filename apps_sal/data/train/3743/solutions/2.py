def chess_board(rows, cols):
    return [['X' if (y + x) % 2 else 'O' for x in range(cols)] for y in range(rows)]
