def display_board(board, width):
    line = f"\n{'-' * (4 * width - 1)}\n"
    return line.join(('|'.join((f' {c} ' for c in row)) for row in (board[i:i + width] for i in range(0, len(board), width))))
