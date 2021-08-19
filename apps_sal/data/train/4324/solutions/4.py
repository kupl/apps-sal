def display_board(board, width):
    return ('\n' + '-' * (4 * width - 1) + '\n').join(['|'.join([' ' + board[i * width + j] + ' ' for j in range(width)]) for i in range(int(len(board) / width))])
