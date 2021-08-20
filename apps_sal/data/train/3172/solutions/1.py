fen_notation = 'rnbqkbnrpc/CPRNBQKBNR'
chess_board = '♖♘♗♕♔♗♘♖♙＿\n▇♟♜♞♝♛♚♝♞♜'
table = dict(list(zip(fen_notation, chess_board)))


def parse_fen(fen_string):

    def rev(p):
        return p[1][::(-1) ** (p[0] % 2)]
    board = list('/'.join(map(rev, enumerate(['Cc' * 4] * 8))))
    (idx, (game, turn)) = (0, fen_string.split()[:2])
    for c in game:
        if c.isdigit():
            idx += int(c)
        else:
            board[idx] = c
            idx += 1
    return rev((turn == 'b', ''.join(map(table.get, board)))) + '\n'
