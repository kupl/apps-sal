LETTERS        = 'abcdefgh'                                                    # Defining some constants
NUMBERS        = '87654321'
W, B = WB      = 'Pp'
EMPTY, CAPTURE = '.x'
WHITEHOME      = '12'
BLACKHOME      = '87'
JUMP           = '54'

def pawn_move_tracker(moves):
    board = {letter + number :                                                 # Representing board as
             B if number == BLACKHOME[1] else                                  # a dictionary for easy
             W if number == WHITEHOME[1] else EMPTY                            # access
             for letter in LETTERS for number in NUMBERS}
    whitemove = True                                                           # Move side switcher
    for move in moves:
        target    = move[-2:]                                                  # Finding target
        mover     = move[0] + str(int(move[-1]) + 1 - whitemove * 2)           # Finding mover
        if  move[-1] in JUMP[whitemove] and board[mover] == EMPTY:             # Mover for the jump
            mover = move[0] + str(int(move[-1]) + 2 - whitemove * 4)
        if (move[-1] in (BLACKHOME, WHITEHOME)[whitemove]           or         # Is the move valid?
            board[target] != (EMPTY, WB[whitemove])[move[1] == CAPTURE] or
            board[mover]  != WB[not whitemove]):
            return "{} is invalid".format(move)
        whitemove = not whitemove                                                  # Switching side
        board[mover]  = EMPTY                                                      # Empty the source cell
        board[target] = WB[whitemove]                                              # Fill the target
    return [[board[letter + number] for letter in LETTERS] for number in NUMBERS]  # Return representation
