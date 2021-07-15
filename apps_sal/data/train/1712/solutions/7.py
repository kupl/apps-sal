def puzzle_solver(li, width, height):
    
    # save pieces of puzzle for later use
    id_number = {i[:2]: i[2] for i in li}
    li, puzzle = list(id_number.keys()), [[() for _ in range(width)] for _ in range(height)] 
    left, right, top, bottom, rest = [], [], [], [], []
    
    # set fixed corners and store sub grid to their correct place
    for grid in li:
        nones, nn = sum(i.count(None) for i in grid), (None, None)
        if nones == 3:
            x, y = [(-1, -1), (-1, 0), (0, -1), (0, 0)][next(i for i, j in enumerate(sum(grid, ())) if j is not None)]
            puzzle[x][y] = grid
        elif nones == 2:
            use = bottom if grid[1] == nn else top if grid[0] == nn else left if (grid[0][0], grid[1][0]) == nn else right
            use.append(grid)
        else:
            rest.append(grid)
    
    # function to set all sidelines
    def set_row(line, start, i, j, o, p, till):
        lookup = {k[o][p]: k for k in line}
        decide = lambda x: {(1, 1, 1, 0): (0, x), (0, 1, 0, 0): (-1, x), (1, 1, 0, 1): (x, 0)}.get((i, j, o, p), (x, -1))
    
        for k in range(1, till - 1):
            x, y = decide(k)
            puzzle[x][y] = lookup[start[i][j]]
            start = puzzle[x][y]
    
    # set all side lines
    for line, start, i, j, o, p, till in [(top, puzzle[0][0], 1, 1, 1, 0, width),
                                          (bottom, puzzle[-1][0], 0, 1, 0, 0, width),
                                          (left, puzzle[0][0], 1, 1, 0, 1, height),
                                          (right, puzzle[0][-1], 1, 0, 0, 0, height)]:
        set_row(line, start, i, j, o, p, till)
    
    #now, all easy set rest of puzzle
    prev = puzzle[0]
    lookup = {k[0]: k for k in rest}
    for k in range(1, height - 1):
        for l in range(1, width - 1):
            puzzle[k][l] = lookup[prev[l][1]]
        prev = puzzle[k]
  
    return [tuple([id_number[j] for j in i]) for i in puzzle]
