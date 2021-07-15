def chess_knight(cell):
    return sum( 1 <= ord(cell[0])-96+d1 <= 8 and 1 <= int(cell[1])+d2 <= 8 for h in [2,-2] for w in [1,-1] for d1,d2 in [(h,w), (w,h)] )
