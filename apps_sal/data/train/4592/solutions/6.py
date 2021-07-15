def print_board(board):
    for x in board:
        for y in x:
            for z in y:
                print(z,end=' ')
            print()
        print()

def check_if_win(board, x, y, z):
    diags = [
    [(0,0,0), (1,1,1), (2,2,2), (3,3,3)],
    [(0,0,3), (1,1,2), (2,2,1), (3,3,0)],
    [(0,3,0), (1,2,1), (2,1,2), (3,0,3)],
    [(0,3,3), (1,2,2), (2,1,1), (3,0,0)],
    
    [(0,0,0), (0,1,1), (0,2,2), (0,3,3)],
    [(0,0,3), (0,1,2), (0,2,1), (0,3,0)],
    [(1,0,0), (1,1,1), (1,2,2), (1,3,3)],
    [(1,0,3), (1,1,2), (1,2,1), (1,3,0)],
    [(2,0,0), (2,1,1), (2,2,2), (2,3,3)],
    [(2,0,3), (2,1,2), (2,2,1), (2,3,0)],
    [(3,0,0), (3,1,1), (3,2,2), (3,3,3)],
    [(3,0,3), (3,1,2), (3,2,1), (3,3,0)]
    ]
    
    for diag in diags:
        if (x,y,z) in diag:
            d = []
            for i,j,k in diag:
                d.append(board[i][j][k])
            if diag[0] != '_' and are_the_same(d): return True
    
    hold_xy = []
    hold_yz = []
    hold_xz = []
    
    for i in range(4):
        hold_xy.append(board[x][y][i])
        hold_yz.append(board[i][y][z])
        hold_xz.append(board[x][i][z])
    
    if hold_xy[0] != '_' and are_the_same(hold_xy): return True
    if hold_yz[0] != '_' and are_the_same(hold_yz): return True
    if hold_xz[0] != '_' and are_the_same(hold_xz): return True
    
    return False

def are_the_same(array):
    first = array[0]
    for c in array[1:]:
        if first != c: return False
    return True

def play_OX_3D(moves):
    P=({},{})
    for counter,(x,y,z) in enumerate(moves,1):
        A=(x,x,y,x  ,x  ,y  ,y  ,z  ,z  ,x+y,y+x,z+x,x-y)
        B=(y,z,z,y+z,y-z,x+z,x-z,x+y,x-y,x+z,y+z,z+y,y-z)
        C=P[counter%2]
        for x in zip(range(13),A,B):C[x]=C.get(x,0)+1
        if 4 in C.values():return'XO'[counter%2]+' wins after %d moves'%counter
    return'No winner'
    
def play_OX_3DS(moves):
    turn = 'O'
    counter = 0
    board = [[['_' for k in range(4)] for j in range(4)] for i in range(4)]
    
    for move in moves:
        x,y,z = move
        board[x][y][z] = turn
        counter += 1
        
        if check_if_win(board, x, y, z):
            return f'{turn} wins after {counter} moves'
            
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'
            
        print_board(board)
        print(counter)
    
    return 'No winner'
