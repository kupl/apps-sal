def chess_bishop_dream(board_size, init_position, init_direction, k):
    ((h, w), (i, j), (di, dj)) = (board_size, init_position, init_direction)
    ((qi, ri), (qj, rj)) = (divmod(i + di * k, h), divmod(j + dj * k, w))
    return [h - 1 - ri if qi % 2 else ri, w - 1 - rj if qj % 2 else rj]
