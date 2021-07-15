from math import ceil,log2
def dithering(width, height):
    size=ceil(log2(max(width,height)))
    grid=[(0,0),(1,1),(1,0),(0,1)]
    add=2
    for i in range(size-1):
        g=[]
        for gg in grid:
            g.append(gg)
            g.append((gg[0]+add,gg[1]+add))
            g.append((gg[0]+add,gg[1]))
            g.append((gg[0],gg[1]+add))
        grid=g; add*=2
    for i in range(len(grid)-1,-1,-1):
        if grid[i][0]>=width or grid[i][1]>=height:
            del grid[i]
    return iter(grid)
