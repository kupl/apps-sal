def path_finder(maze): #IMPLEMENTING BFS ALGORITHM
    mtx = list(map(list, maze.splitlines())) #convert string to 2d array
    R = len(mtx[0]) #number of rows or size of te mtx
    mtx[R-1][R-1] = 'E' #define the exit as 'E'
    sr, sc = 0, 0 #starting node
    rq, cq = [], [] #empty queue for row and column
    prev = [[' ']*(R) for x in range(R)]
    
    move_count = 0 
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    
    reached_end = False # variable used to know if exit is reached
    
    visited = [[False]*(R) for x in range(R)] # Mtx to know if node visited 
    
    dr = [-1, 1, 0, 0] # North, South, West direction vectors
    dc = [0, 0, 1, -1] # North, South, West direction vectors
    
    rq.append(sr)
    cq.append(sc)

    visited[sr][sc] = True
    while len(rq):
        r = rq.pop(0)
        c = cq.pop(0)

        if mtx[r][c] == 'E':
            reached_end = True #The end has been reached
            return move_count

        for i in range(4): #     explore_neighbours
            rr = r + dr[i]
            cc = c + dc[i]

            if rr < 0 or cc< 0: continue
            if rr >= R or cc >= R: continue
            
            if visited[rr][cc]: continue
            if mtx[rr][cc] == 'W': continue
            
            rq.append(rr)
            cq.append(cc)
            visited[rr][cc] = True
            prev[rr][cc] = [r,c] # keep track of the parent 
            nodes_in_next_layer += 1
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    else:
        return False
