def is_solved(board):
    curr = 0;
    for r in board:
        for c in r:
            if c != curr:
                return False;
            curr+=1;
    return True;
