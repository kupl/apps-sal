BOARD = '▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇\n▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇\n▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇\n▇＿▇＿▇＿▇＿\n＿▇＿▇＿▇＿▇'
PIECES = dict(zip('kqrbnpKQRBNP', '♔♕♖♗♘♙♚♛♜♝♞♟'))


def parse_fen(string):
    board = list(map(list, BOARD.splitlines()))
    (pieces, color) = string.split()[:2]
    for (r, rank) in enumerate(pieces.split('/')):
        f = 0
        for square in rank:
            if square.isdigit():
                f += int(square)
            else:
                board[r][f] = PIECES[square]
                f += 1
    return '\n'.join(map(''.join, board if color == 'w' else [rank[::-1] for rank in board[::-1]])) + '\n'
