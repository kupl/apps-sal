def display_board(board, width):
    n = int(len(board) / width)
    sep = '\n' + '-' * (4 * width - 1) + '\n'
    return sep.join([' ' + ' | '.join(board[i * width:(i + 1) * width]) + ' ' for i in range(n)])
