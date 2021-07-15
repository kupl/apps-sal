LETTERS        = 'abcdefgh'
NUMBERS        = '87654321'
W, B = WB      = 'Pp'
EMPTY, CAPTURE = '.x'
WHITEHOME      = '12'
BLACKHOME      = '87'
JUMP           = '54'

def pawn_move_tracker(moves):
    board = {letter + number :
             B if number == BLACKHOME[1] else W if number == WHITEHOME[1] else EMPTY
             for letter in LETTERS for number in NUMBERS}
    whitemove = True
    for move in moves:
        target    = move[-2:]
        mover     = move[0] + str(int(move[-1]) + 1 - whitemove * 2)
        if  move[-1] in JUMP[whitemove] and board[mover] == EMPTY:
            mover = move[0] + str(int(move[-1]) + 2 - whitemove * 4)
        if (move[-1] in (BLACKHOME, WHITEHOME)[whitemove]           or
            board[target] != (EMPTY, WB[whitemove])[move[1] == CAPTURE] or
            board[mover]  != WB[not whitemove]):
            return "{} is invalid".format(move)
        whitemove = not whitemove
        board[mover]  = EMPTY
        board[target] = WB[whitemove]
    return [[board[letter + number] for letter in LETTERS] for number in NUMBERS]

