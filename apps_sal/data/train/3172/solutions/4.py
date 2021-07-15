def parse_fen(string):
    placement, active, *_ = string.split()
    board = []
    for color, pieces in enumerate(placement.split('/')):
        color %= 2
        rank = []
        for piece in pieces:
            if piece.isdigit():
                spaces = int(piece)
                for i in range(spaces): rank.append(empty[(color+i)%2])
                color ^= spaces % 2
            else:
                rank.append(symbols[piece])
                color ^= 1
        board.append(rank)
    d = 1 if active == 'w' else -1
    return '\n'.join(''.join(c for c in rank[::d]) for rank in board[::d]) + '\n'

symbols = dict(list(zip('PNBRQKpnbrqk', '♟♞♝♜♛♚♙♘♗♖♕♔')))
empty = '▇＿'

