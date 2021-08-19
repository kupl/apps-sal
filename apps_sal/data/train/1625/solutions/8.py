def pawn_move_tracker(moves):
    white_pawns = [(x, 2) for x in range(1, 9)]
    black_pawns = [(x, 7) for x in range(1, 9)]
    all_pawns = (white_pawns, black_pawns)
    turn = 0
    for move in moves:
        pawns = all_pawns[turn]
        opponent = all_pawns[turn ^ 1]
        direction = 1 - 2 * turn
        capture = 'x' in move
        if capture:
            (sx, dx, dy) = (column(move[0]), column(move[2]), int(move[3]))
            if (dx, dy) in opponent:
                opponent.remove((dx, dy))
            else:
                return f'{move} is invalid'
        else:
            sx = dx = column(move[0])
            dy = int(move[1])
            if (dx, dy) in opponent or (dx, dy - direction) in opponent:
                return f'{move} is invalid'
        sy = dy - direction
        if not capture and dy == (4, 5)[turn] and (not (sx, sy) in pawns):
            sy -= direction
        if (sx, sy) not in pawns:
            return f'{move} is invalid'
        pawns.remove((sx, sy))
        pawns.append((dx, dy))
        turn ^= 1

    def char(p):
        return 'P' if p in white_pawns else 'p' if p in black_pawns else '.'
    return [[char((x, y)) for x in range(1, 9)] for y in range(8, 0, -1)]


def column(c):
    return ' abcdefgh'.index(c)
