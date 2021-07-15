def get_password(grid,directions):
    #generate start point
    start = [[k,x] for k,v in enumerate(grid) for x,y in enumerate(v) if y=='x'][0]
    curr = start
    a = ''
    for i in directions:
        if i[-1] == 'T':
            if i == 'leftT':
                curr[1] -= 1
                a+= grid[curr[0]][curr[1]]
            if i == 'rightT':
                curr[1] += 1
                a+= grid[curr[0]][curr[1]]
            if i == 'upT':
                curr[0] -= 1
                a+= grid[curr[0]][curr[1]]
            if i == 'downT':
                curr[0] += 1 
                a+= grid[curr[0]][curr[1]]
        if i[-1] != 'T':
            if i == 'left':
                curr[1] -= 1
            if i == 'right':
                curr[1] += 1
            if i == 'up':
                curr[0] -= 1
            if i == 'down':
                curr[0] += 1
    return a    

    
                

