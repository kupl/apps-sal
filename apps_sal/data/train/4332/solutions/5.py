def langtons_ant(n):
    if n == 0: return 0
    
    width, height, i, j = 150, 150, 75, 75
    
    grid = [[1] * width for i in range(height)]
    
    directions = list(range(4))
    
    d, count, s, black = 0, 0, 0, []
    
    while count < n and 0 <= i < height and 0 <= j < width: 
        cell = grid[i][j]
        turn = -1 if cell == 0 else 1
        
        if cell: 
            grid[i][j] = 0
            s += 1            
        else: 
            grid[i][j] = 1
            s -= 1
            
        black.append(s)
        d = directions[(4 + d + turn) % 4]
        
        if d == 0: i -= 1
        elif d == 1: j -= 1
        elif d == 2: i += 1
        elif d == 3: j += 1        
        
        count += 1
    
    limit, period = 10000, 104
    
    if count <= limit + period + 1: return black[-1]
        
    diff = black[limit + period] - black[limit]
    cycles, r = divmod(n - 1 - limit, period)
    
    return black[limit + r] + cycles * diff
