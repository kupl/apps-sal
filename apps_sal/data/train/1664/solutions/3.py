def amazon_check_mate(king, amazon):
    if king == amazon:
        return []
    king_pos = [ord(king[1]) - ord('1'), ord(king[0]) - ord('a')]
    amazon_pos = [ord(amazon[1]) - ord('1'), ord(amazon[0]) - ord('a')]
    board = [[' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8]
    board[king_pos[0]][king_pos[1]] = 'K'
    board[amazon_pos[0]][amazon_pos[1]] = 'A'
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1], [1, 2], [2, 1], [1, -2], [2, -1], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
    for i in range(8):
        (row, col) = (king_pos[0] + dirs[i][0], king_pos[1] + dirs[i][1])
        if 0 <= row < 8 and 0 <= col < 8:
            board[row][col] = 'B' if board[row][col] == ' ' else 'C'
    for i in range(16):
        (row, col) = (amazon_pos[0] + dirs[i][0], amazon_pos[1] + dirs[i][1])
        while 0 <= row < 8 and 0 <= col < 8 and (board[row][col] in [' ', 'B']):
            if board[row][col] == ' ':
                board[row][col] = 'X'
            if 8 <= i:
                break
            (row, col) = (row + dirs[i][0], col + dirs[i][1])
    res = [0, 0, 0, 0]
    for row in range(8):
        for col in range(8):
            if board[row][col] not in ['K', 'B', 'A', 'C']:
                check = board[row][col] == 'X'
                valid_around = 0
                for i in range(8):
                    (row_, col_) = (row + dirs[i][0], col + dirs[i][1])
                    if 0 <= row_ < 8 and 0 <= col_ < 8 and (board[row_][col_] in [' ', 'A']):
                        valid_around += 1
                if check:
                    res[0 if valid_around == 0 else 1] += 1
                elif valid_around == 0:
                    res[2] += 1
                else:
                    res[3] += 1
    return res
