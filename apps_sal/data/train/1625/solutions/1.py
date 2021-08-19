def pawn_move_tracker(moves):
    board = [[c] * 8 for c in '.p....P.']
    for (turn, move) in enumerate(moves, 1):
        (capture, white_turn) = (len(move) == 4, turn % 2)
        direction = 2 * white_turn - 1
        (c0, _, c, r) = (move * 2)[:4]
        (c0, c, r) = (ord(c0) - ord('a'), ord(c) - ord('a'), 8 - int(r))
        long_move = not capture and r == 3 + white_turn
        for i in range(1, 2 + long_move):
            r0 = r + direction * i
            if board[r0][c0][0] == 'pP'[white_turn] and board[r][c][0] == '.pP'[capture and 2 - white_turn]:
                (board[r0][c0], board[r][c]) = ('.', board[r0][c0])
                break
        else:
            return '{} is invalid'.format(move)
    return board
