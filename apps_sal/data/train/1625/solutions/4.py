def pawn_move_tracker(moves):

    def getSourcePos(m, delta):  return m[0] + str(int(m[-1]) + delta * comingFrom[player])
    
    ROWS, COLS = "87654321", "abcdefgh"                                                          # constants...
    comingFrom, mayBeDouble = {'P': -1, 'p': 1}, {'P': '4', 'p': '5'}                            # constants...
    
    pawns = {'P': {y+"2" for y in COLS}, 'p': {y+"7" for y in COLS}}                             # All pawns at their initial position
    for t,m in enumerate(moves):
        player, other, toMove = "Pp"[t%2], "pP"[t%2], set()
        
        toMove.add(getSourcePos(m, 1))                                                           # Single move or capturing pawn
        if m[1] == mayBeDouble[player] and m[1]!='x':  toMove.add(getSourcePos(m, 2))            # Double move if m in row 4 or 5, according to "player" (only if not capturing move for m)
        toMove &= pawns[player]                                                                  # Extract matching pawn(s)
        
        if ( m[1] == 'x' and m[2:] not in pawns[other] or m[1] != 'x' and m in pawns[other]      # Invalid if capturing non-existing enemy or moving to a position occupied by enemy...
          or m in pawns[player] or len(toMove) != 1):                                            # ... or moving to a position occupied by friend or no pawn to move or too many.
            return "{} is invalid".format(m)
        
        if m[1] == 'x':
            m = m[2:]; pawns[other].remove(m)                                                    # Reassign final position (needed if capture) and remove captured enemy piece
        pawns[player].remove(toMove.pop())                                                       # Move current pawn (remove/add) 
        pawns[player].add(m)
            
    board = {pos: k for k,s in pawns.items() for pos in s}                                       # Dict of all remaining pawns and their position
    return [[board.get(y+x, '.') for y in COLS] for x in ROWS]                                   # final board
