def is_solved(board):
    return all( v==w for x,r in enumerate(board) for w,v in enumerate(r,x*len(board)) )
