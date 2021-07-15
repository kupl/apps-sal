from itertools import takewhile,count

def get_diagonale_code(grid):
    grid = grid.replace(' ','').split('\n')
    rail = len(grid)-1
    return grid[0] if not rail else ''.join(takewhile(bool, genRail(grid,rail)))

def genRail(grid,rail):
    for i in count():
        n,x = divmod(i,rail)
        row = rail-x if n&1 else x
        yield '' if i>=len(grid[row]) else grid[row][i]
