def chess_bishop_dream(board_size, init_position, init_direction, k):
    (l, (m, n), (x, y), (dx, dy)) = (0, board_size, init_position, init_direction)
    while k:
        k -= 1
        l += 1
        x += dx
        y += dy
        if x < 0 or x == m:
            dx = -dx
            x += dx
        if y < 0 or y == n:
            dy = -dy
            y += dy
        if [x, y] == init_position and [dx, dy] == init_direction:
            k %= l
    return [x, y]
