BOARD = '▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇\n▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇\n▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇\n▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇'
PIECES = dict(zip('kqrbnpKQRBNP', '♔♕♖♗♘♙♚♛♜♝♞♟'))


def parse_fen(string):
    board = list(map(list, BOARD.splitlines()))
    pieces, color, *_ = string.split()

    i = 0 if color == 'w' else 7

    for r, rank in enumerate(pieces.split('/')):
        f = 0
        for square in rank:
            if square.isdigit():
                f += int(square)
            else:
                board[abs(r - i)][abs(f - i)] = PIECES[square]
                f += 1
    return '\n'.join(map(''.join, board)) + '\n'
