def find_word(board, word, cursor=None):
    if not word:
        return True
    workboard = [row[:] for row in board]
    (sy, sx, ey, ex) = (0, 0, len(board), len(board[0]))
    if cursor:
        (cx, cy) = cursor
        workboard[cy][cx] = '-'
        sy = max(sy, cy - 1)
        sx = max(sx, cx - 1)
        ey = min(ey, cy + 2)
        ex = min(ex, cx + 2)
    for (y, row) in enumerate(workboard[:ey][sy:]):
        for (x, cell) in enumerate(row[:ex][sx:]):
            if cell == word[0] and find_word(workboard, word[1:], (x + sx, y + sy)):
                return True
    return False
