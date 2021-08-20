def chess_bishop_dream(board_size, init_position, init_direction, k):
    (m, n) = board_size
    (x, y) = init_position
    (dx, dy) = init_direction
    r = [[x, y]]
    while True:
        (x, y) = (x + dx, y + dy)
        if not 0 <= x < m:
            x += -dx
            dx = -dx
        if not 0 <= y < n:
            y += -dy
            dy = -dy
        r.append([x, y])
        if len(r) > 2 and r[:2] == r[-2:]:
            break
    r = r[:-2]
    return r[k % len(r)]
