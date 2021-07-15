import numpy as np
def pawn_move_tracker(moves):
    
    print(moves)
    board = [
    [".",".",".",".",".",".",".","."],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    ["P","P","P","P","P","P","P","P"],
    [".",".",".",".",".",".",".","."]
    ]
    
    board = np.asarray(board)
    white = True
    cols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    

    for move in moves:
        if white:
            diff, piece, start = 1, 'P', 6
        else:
            diff, piece, start = -1, 'p', 1
            
        if 'x' in move:
            splt = move.split('x')
            new_c, new_r = cols[splt[1][0]], 8 - int(splt[1][1]) 
            old_c, old_r = cols[splt[0]], new_r + diff
            if board[old_r,old_c] != piece or board[new_r, new_c] in ['.',piece]:
                return move + ' is invalid'
            else:
                board[old_r,old_c]  = '.'
                board[new_r, new_c] = piece
        else:
            col, new_row = cols[move[0]], 8 - int(move[1]) 
            if board[new_row,col] != '.':
                return move + ' is invalid'
            
            x = np.where(board == piece)
            
            pwns = list((zip(x[0],x[1])))
            if (new_row + diff, col) in pwns:
                board[new_row + diff, col] = '.'
                board[new_row, col] = piece
            elif new_row + 2*diff == start:
                if (new_row + 2*diff, col) in pwns:
                    board[new_row + 2*diff, col] = '.'
                    board[new_row, col] = piece
            else:
                return move + ' is invalid'
                
                
                
        if white:
            white = False
        else:
            white = True

    
    return np.ndarray.tolist(board)
