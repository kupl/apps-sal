def pawn_move_tracker(moves):
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
    turn = 0
    for p in moves:
        if len(p) == 2:
            x,y = 'abcdefgh'.index(p[0]), 8-int(p[1])
            if board[y][x]!='.': return p+' is invalid'
            if turn == 0:
                if y<7 and board[y+1][x] == 'P': board[y][x]='P'; board[y+1][x]='.'
                elif y==4 and board[y+1][x] == '.' and board[y+2][x] == 'P': board[y][x]='P'; board[y+2][x]='.'
                else: return p+' is invalid'
            else:
                if y>0 and board[y-1][x] == 'p': board[y][x]='p'; board[y-1][x]='.'
                elif y==3 and board[y-1][x] == '.' and board[y-2][x] == 'p': board[y][x]='p'; board[y-2][x]='.'
                else: return p+' is invalid'
        else:
            x,y,fx,fy = 'abcdefgh'.index(p[2]), 8-int(p[3]), 'abcdefgh'.index(p[0]), 8-int(p[3])+(1-turn*2)
            if turn == 0:
                if board[y][x]=='p' and board[fy][fx]=='P': board[y][x]='P'; board[fy][fx]='.'
                else: return p+' is invalid'
            else:
                if board[y][x]=='P' and board[fy][fx]=='p': board[y][x]='p'; board[fy][fx]='.'
                else: return p+' is invalid'
        turn ^= 1
    return board
