def check_victory(board):
    size = len(board)
    depth_sums = [[0] * size for i in range(size)]
    down_cross_sums = [[0, 0] for i in range(size)]
    side_cross_sums = [[0, 0, 0, 0] for i in range(2)]
    diag_sums = [[0, 0], [0, 0]]
    for z in range(0, size):
        col_sums = [0] * size
        front_cross_sums = [0, 0]
        for y in range(0, size):
            row_sum = 0
            for x in range(0, size):
                val = board[z][y][x]
                row_sum += val
                col_sums[x] += val
                depth_sums[y][x] += val
                if x == y:
                    front_cross_sums[0] += val
                    if y == z:
                        diag_sums[0][0] += val
                    if y + z == size - 1:
                        diag_sums[1][0] += val
                if x == z:
                    down_cross_sums[y][0] += val
                if x + z == size - 1:
                    down_cross_sums[y][1] += val
                if y == z:
                    side_cross_sums[0][x] += val
                if y + z == size - 1:
                    side_cross_sums[1][x] += val
                if x + y == size - 1:
                    front_cross_sums[1] += val
                    if y == z:
                        diag_sums[0][1] += val
                    if y + z == size - 1:
                        diag_sums[1][1] += val
                if row_sum == size or col_sums[x] == size or front_cross_sums[0] == size or (front_cross_sums[1] == size) or (depth_sums[y][x] == size) or (down_cross_sums[y][0] == size) or (down_cross_sums[y][1] == size) or (side_cross_sums[0][x] == size) or (side_cross_sums[1][x] == size) or (diag_sums[0][0] == size) or (diag_sums[0][1] == size) or (diag_sums[1][0] == size) or (diag_sums[1][1] == size):
                    return 1
                if row_sum == -size or col_sums[x] == -size or front_cross_sums[0] == -size or (front_cross_sums[1] == -size) or (depth_sums[y][x] == -size) or (down_cross_sums[y][0] == -size) or (down_cross_sums[y][1] == -size) or (side_cross_sums[0][x] == -size) or (side_cross_sums[1][x] == -size) or (diag_sums[0][0] == -size) or (diag_sums[0][1] == -size) or (diag_sums[1][0] == -size) or (diag_sums[1][1] == -size):
                    return -1
    return 0


def play_OX_3D(moves):
    board = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
    move_cnt = 0
    play_num = 1
    for move in moves:
        board[move[2]][move[1]][move[0]] = play_num
        move_cnt += 1
        victor = check_victory(board)
        if victor >= 1:
            print(moves)
            return 'O wins after ' + str(move_cnt) + ' moves'
        if victor <= -1:
            print(moves)
            return 'X wins after ' + str(move_cnt) + ' moves'
        play_num *= -1
    print(moves)
    return 'No winner'
