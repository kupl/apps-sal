from itertools import count

ALL_MOVES  = [(1,1), (0,1), ( 1,0), (-1,0), (0,-1), (-1,1), ( 1,-1), (-1,-1)]       # Natural directions of moves for king or queen (one step)
AMA_MOVES  = [(1,2), (2,1), (-1,2), (2,-1), (1,-2), (-2,1), (-1,-2), (-2,-1)]       # Knight moves for amazon queen


def amazon_check_mate(*args):

    def posInBoard(x,y):  return 0 <= x < 8 and 0 <= y < 8
    
    def getCoveredPos(start, king=None):                                            # Working with the amazon queen is king is provided
        covered = {start}
        for m in (AMA_MOVES if king else ALL_MOVES):                                # All "one step" moves (either for queen or king)
            pos = tuple( z+dz for z,dz in zip(start,m) )
            if posInBoard(*pos): covered.add(pos)
        
        if king:                                                                    # Get long range moves, for queen only (meaning: if king is provided!)
            for dx,dy in ALL_MOVES:
                for n in count(1):
                    pos = (start[0]+dx*n, start[1]+dy*n)
                    if not posInBoard(*pos) or pos == king: break                   # Abort if not in board or if white king is on the way
                    covered.add(pos)
        
        return covered
    
    
    K, Q      = [(ord(s[0])-97, ord(s[1])-49) for s in args]                   # King and Queen positions as tuples
    kCover    = getCoveredPos(K)                                                    # Positions protected by white king
    fullCover = getCoveredPos(Q,K) | kCover                                         # All position protected by white pieces
    freeQueen = Q not in kCover                                                     # Queen not protected by king
    counts    = [0] * 4                                                             # Indexes: 2 * "is not check" + 1 * "safe position available around"
    
    for x in range(8):
        for y in range(8):
            black = (x,y)
            
            if black in kCover or black == Q: continue                              # No adjacent kings and no king copulating with an amazon...
            
            safePosAround = any( posInBoard(*neigh) and (neigh not in fullCover or neigh == Q and freeQueen)   # Neighbour is in board and is a safe place or is the queen and isn't protected by white king
                                 for neigh in ((x+dx, y+dy) for dx,dy in ALL_MOVES) )
                                    
            counts[ 2*(black not in fullCover) + safePosAround ] += 1               # Update the correct index of "ans"
            
    return counts

