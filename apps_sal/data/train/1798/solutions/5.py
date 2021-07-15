def get_generation(cells, generations):
    
    if generations == 0: return cells
    
    # avoid checking the whole array
    alive = set((rindex, cindex) for rindex, row 
                 in enumerate(cells) for cindex, cell in enumerate(row) 
                 if cell == 1)
    
    for _ in xrange(generations):
        
        # if a cell has x neighbours, its coordinates will appear x times in list
        neighbours = [(cell[0]+y, cell[1]+x) for cell in alive 
                      for y in xrange(-1, 2) for x in xrange(-1, 2) 
                      if (y, x) != (0, 0)]
        
        # new generation
        alive = set(cell for cell in neighbours 
                    if (neighbours.count(cell) == 3) 
                       or (cell in alive and neighbours.count(cell) == 2))
    
    # rebuild the array around the living cells of the last generation
    ys, xs = zip(*alive)
    
    cells = [[1 if (rindex, cindex) in alive else 0 
              for cindex in range(min(xs), max(xs) + 1)] 
             for rindex in range(min(ys), max(ys) + 1)]
    
    return cells
