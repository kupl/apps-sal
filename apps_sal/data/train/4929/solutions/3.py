def get_diagonale_code(grid: str) -> str:
    grid = grid.split('\n')
    ret = ''
    l , i, s = 0, 0 , 1
    while 1:
        try:
            ret += grid[l][i]
        except:
            return ret
        i += 2
        l += s
        if l == len(grid)-1 or l==0:
            s = -s

