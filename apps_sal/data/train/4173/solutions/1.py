def ant(grid, c, r, n, direction = 0):
    
    MOVES = [(-1,0), (0,1), (1,0), (0,-1)]             # directions the ant can move
    
    dims = {(min, 0): 0, (max, 0): len(grid)-1,        # min and max values of row index
            (min, 1): 0, (max, 1): len(grid[0])-1}     # min and max values of column index
            
    gridWhite = { (x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] }    # set of white squares only
    
    for _ in range(n):                                                  # Ant is at work...
        direction = (direction + (-1)**((r,c) not in gridWhite)) % 4    # shift the ant
        gridWhite ^= {(r,c)}                                            # shift the square
        r += MOVES[direction][0]                                        # update position
        c += MOVES[direction][1]
        for func,dim in dims:
            dims[(func,dim)] = func(dims[(func,dim)], (r,c)[dim])       # update min and max values of the indexes
    
    MinX, MinY = dims[(min,0)], dims[(min,1)]                  # minimum for rows (x) and columns(y)
    lenX, lenY = dims[(max,0)]-MinX+1, dims[(max,1)]-MinY+1    # determine the final dimensions of the grid
    
    return [ [(1 if (x+MinX, y+MinY) in gridWhite else 0) for y in range(lenY)] for x in range(lenX) ]
