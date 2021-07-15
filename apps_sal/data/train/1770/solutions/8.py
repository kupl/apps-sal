def path_finder(maze):
    maze = maze.split('\n')
    x_, y_ = len(maze)-1, len(maze[0])-1
    
    DMap, exit = {(0,0):1}, (x_, y_)
    
    while 1: 
        chkr = len(DMap)
        for x, r in enumerate(maze):
            for y, c in enumerate(r):
                
                if maze[x][y]=='.' and not DMap.get((x,y)):
                    ways = []
                    for e in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        (not DMap.get(e) or ways.append(DMap[e]))
                        
                    if ways:  DMap[(x,y)] = min(ways) + 1
                        
        if chkr == len(DMap): break

    return DMap.get(exit, 1) - 1 

