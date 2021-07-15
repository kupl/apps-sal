def path_finder(maze):

    maze = maze.split('\n')
    n = len(maze) #maze order
    reachable = [[None]*(n+2) for i in range(n+2)] #maze with boundaries
    
    for i in range(n+2): #boundaries are unreachable
        reachable[0][i] = False
        reachable[n+1][i] = False
        reachable[i][0] = False
        reachable[i][n+1] = False
    
    queue = [(1,1)] #start with (1,1)
    
    while queue: #while queue is not empty
        
        i, j = queue.pop(0)
        reachable[i][j] = True
        
        for x, y in (0,1),(0,-1),(-1,0),(1,0): #east-(0,1); west-(0,-1); north-(-1,0); south-(1,0)
            p, q = i+x, j+y
            if reachable[p][q] == None: #spot not visited yet
                if maze[p-1][q-1] == '.': #spot can be visited
                    reachable[p][q] = True
                    queue.append((p,q)) #if spot can be visited look for a path
                else:
                    reachable[p][q] = False #spot can't be visited i.e. wall

    return False if reachable[n][n] == None else reachable[n][n]
