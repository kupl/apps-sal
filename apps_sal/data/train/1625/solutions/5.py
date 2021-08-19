import re


def pawn_move_tracker(moves):
    turn = 0
    white = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
    black = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
    try:
        for move in moves:
            if re.match('[a-h][1-8]', move):
                (white, black) = motion(white, black, move, turn)
            elif re.match('[a-h]x[a-h][1-8]', move):
                (white, black) = eat(white, black, move, turn)
            turn = (turn + 1) % 2
    except ValueError as move:
        return '{0} is invalid'.format(move)
    return pawns_to_board(white, black)


def motion(white, black, move, turn):
    column = move[0]
    row = move[1]
    piece = None
    if turn == 0:
        try:
            search_row = str(int(row) - 1)
            piece = white.index(column + search_row)
        except ValueError:
            try:
                if row == '4':
                    piece = white.index(column + '2')
                else:
                    raise ValueError
            except ValueError:
                raise ValueError(move)
        try:
            black.index(move)
        except ValueError:
            white[piece] = move
        else:
            raise ValueError(move)
    elif turn == 1:
        try:
            search_row = str(int(row) + 1)
            piece = black.index(column + search_row)
        except ValueError:
            try:
                if row == '5':
                    piece = black.index(column + '7')
                else:
                    raise ValueError
            except ValueError:
                raise ValueError(move)
        try:
            white.index(move)
        except ValueError:
            black[piece] = move
        else:
            raise ValueError(move)
    return [white, black]


def eat(white, black, move, turn):
    column = move[0]
    row = move[3]
    piece = None
    dead = None
    if turn == 0:
        try:
            search_row = str(int(row) - 1)
            piece = white.index(column + search_row)
        except ValueError:
            raise ValueError(move)
        else:
            try:
                dead = black.index(move[2:4])
            except ValueError:
                raise ValueError(move)
            else:
                white[piece] = move[2:4]
                del black[dead]
    elif turn == 1:
        try:
            search_row = str(int(row) + 1)
            piece = black.index(column + search_row)
        except ValueError:
            raise ValueError(move)
        else:
            try:
                dead = white.index(move[2:4])
            except ValueError:
                raise ValueError(move)
            else:
                black[piece] = move[2:4]
                del white[dead]
    return [white, black]


def pawns_to_board(white, black):
    board = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
    for i in white:
        (r, c) = coords(i)
        board[r][c] = 'P'
    for i in black:
        (r, c) = coords(i)
        board[r][c] = 'p'
    return board


def coords(pos):
    col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(pos[0])
    row = 8 - int(pos[1])
    return [row, col]
