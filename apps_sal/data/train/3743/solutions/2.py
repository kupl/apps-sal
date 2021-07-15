chess_board = lambda rows, cols: [['X' if (y + x) % 2 else 'O' for x in range(cols)] for y in range(rows)] 
