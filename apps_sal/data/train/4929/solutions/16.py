def get_diagonale_code(grid: str) -> str:
    grid = grid.replace(' ','').split('\n')
    x,y = 0,0
    s=1
    res=''
    try:
        while True:
            print((x,y,s,grid[x][y]))
            res+=grid[x][y]
            y+=1
            x+= 1 if s==1 else -1
            if not 0<=x<len(grid):
                s*=-1
                x+=s*2
    except:
        return res

