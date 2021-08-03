def checker(board, i, j, k, turn):

    return all(n == turn for n in board[i][j]) or \
        all(n == turn for n in [m[k] for m in board[i]]) or \
        all(board[i][n][n] == turn for n in range(4)) or \
        all(board[i][n][3 - n] == turn for n in range(4)) or \
        all(bn[j][k] == turn for bn in board) or \
        all(board[n][n][n] == turn for n in range(4)) or \
        all(board[n][n][3 - n] == turn for n in range(4)) or \
        all(board[n][3 - n][3 - n] == turn for n in range(4)) or \
        all(board[n][3 - n][n] == turn for n in range(4)) or \
        all(board[n][3 - n][k] == turn for n in range(4)) or \
        all(board[n][n][k] == turn for n in range(4)) or \
        all(board[n][j][n] == turn for n in range(4)) or \
        all(board[n][j][3 - n] == turn for n in range(4))


def play_OX_3D(moves):
    board = [[[' ' for _ in range(4)] for _ in range(4)] for _ in range(4)]
    turn = 'O'

    for ind, (i, j, k) in enumerate(moves, 1):
        board[i][j][k] = turn

        if checker(board, i, j, k, turn):
            return f'{turn} wins after {ind} moves'

        turn = 'OX'[turn == 'O']

    return 'No winner'
