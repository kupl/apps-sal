def display_board(board, width):
    row = lambda i: f" {' | '.join(board[i:i+width])} "
    sep = f"\n{'':-^{4 * width - 1}}\n"
    return sep.join(row(i) for i in range(0, len(board), width))
