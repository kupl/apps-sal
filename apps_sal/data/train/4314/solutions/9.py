def chess_bishop_dream(size, init_pos, init_dir, k):
    pos = init_pos.copy()
    dir = init_dir.copy()
    i = k
    while i > 0:
        check = [0 <= pos[0] + dir[0] < size[0], 0 <= pos[1] + dir[1] < size[1]]
        pos[0] += dir[0] * check[0]
        pos[1] += dir[1] * check[1]
        dir[0] *= int((int(check[0]) - 0.5) * 2)
        dir[1] *= int((int(check[1]) - 0.5) * 2)
        i -= 1
        if pos == init_pos and dir == init_dir:
            i %= k - i
    return pos
