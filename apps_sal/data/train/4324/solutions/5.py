def display_board(board, width):
    lines = [' ' + ' | '.join(board[i:i+width]) + ' ' for i in range(0, len(board), width)]
    return ('\n' + '-' * len(lines[0]) + '\n').join(lines)
