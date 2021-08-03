def chess_bishop_dream(bs, init_pos, init_dir, k):

    pos, dir = init_pos[:], init_dir[:]
    n, start = k, (init_pos, init_dir)
    while n:
        pos = [x + dx for x, dx in zip(pos, dir)]
        for i in range(2):
            if not (0 <= pos[i] < bs[i]):
                dir[i] *= -1
                pos[i] = [0, bs[i] - 1][pos[i] > 0]
        n -= 1
        if start == (pos, dir):
            n %= k - n

    return pos
