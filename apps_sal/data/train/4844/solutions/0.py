MOVES = {"right": (0,1), "down": (1,0), "left": (0,-1), "up": (-1,0)}


def get_password(grid, dirs):
    x,y = next( (x,y) for x,r in enumerate(grid) for y,c in enumerate(r) if c=='x' )
    pwd = []
    for d in dirs:
        dx,dy = MOVES[d.strip('T')]
        x,y = x+dx,y+dy
        if d.endswith('T'): pwd.append(grid[x][y])
    return ''.join(pwd)
