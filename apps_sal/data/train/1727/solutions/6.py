def find_word(board, s):
    
    def seekFrom(x,y):
        bd[x][y] = ''
        ret = next(dfs(x,y), False)
        bd[x][y] = s[0]
        return ret
    
    def dfs(x,y,i=1):
        if i==len(s): yield True
        else:
            candidates = ( (x+dx,y+dy) for dx in range(-1,2) for dy in range(-1,2) 
                                       if (dx or dy) and 0<=x+dx<len(bd) and 0<=y+dy<len(bd[0]) and bd[x+dx][y+dy]==s[i] )
            for a,b in candidates:
                bd[a][b] = ''
                yield from dfs(a,b,i+1)
                bd[a][b] = s[i]
    
    bd = list(map(list, board))
    return any( seekFrom(x,y) for x,r in enumerate(board) for y,c in enumerate(r) if c==s[0] )
