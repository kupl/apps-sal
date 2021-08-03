def find_word(board, word, trail=None):
    if not word:
        return True
    if not trail:
        board = {(row, col): item for row, line in enumerate(board) for col, item in enumerate(line)}
        valid_first = [k for k, v in list(board.items()) if v == word[0]]
        return any(find_word(board, word[1:], [coord]) for coord in valid_first)
    else:
        x, y = trail[-1]
        neighbors = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        valid_next = [p for p in neighbors if p in board and p not in trail and board[p] == word[0]]
        return any(find_word(board, word[1:], trail + [coord]) for coord in valid_next)
