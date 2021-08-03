def chess_bishop_dream(board_size, pos, dir, k):
    k %= ((board_size[0]) * (board_size[1]) * 2)
    steps = 0
    while steps < k:
        print(pos, steps, k, dir)
        rows_to_go = pos[0] if dir[0] == -1 else (board_size[0] - pos[0] - 1)
        cols_to_go = pos[1] if dir[1] == -1 else (board_size[1] - pos[1] - 1)
        n = min(rows_to_go, cols_to_go, k - steps)
        steps += n
        pos = [pos[0] + n * dir[0], pos[1] + n * dir[1]]
        if steps == k:
            break
        next_pos = [pos[0] + dir[0], pos[1] + dir[1]]
        valid_row = (0 <= next_pos[0] < board_size[0])
        valid_col = (0 <= next_pos[1] < board_size[1])
        if valid_col:
            dir[0] *= -1
            pos[1] = next_pos[1]
        elif valid_row:
            dir[1] *= -1
            pos[0] = next_pos[0]
        else:
            dir[0] *= -1
            dir[1] *= -1
        steps += 1
    return pos
