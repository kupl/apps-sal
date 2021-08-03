class Solution(object):

    def shortestPath(self, grid, k):
        \"\"\"
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        \"\"\"
        def getNei(x,y):
            if x+1 < m:
                yield x+1,y,grid[x+1][y]
            if y+1 < n:
                yield x,y+1,grid[x][y+1]
            if x>0:
                yield x-1,y,grid[x-1][y]
            if y>0:
                yield x,y-1,grid[x][y-1]
                
        m,n = len(grid),len(grid[0])
        cost = [[float('inf')]*n for _ in range(m)]
        cost[0][0] = 0
        #x,y,steps,cost left
        q = collections.deque([(0,0,0,k)])
        while q:
            x,y,steps,rem = q.popleft()            
            for x1,y1,blocked in getNei(x,y):
                cost2 = steps+1
                if rem-blocked >= 0 and cost2 < cost[x1][y1]:
                    cost[x1][y1] = cost2
                    if blocked:
                        q.append((x1,y1,cost2,rem-blocked))
                    else:
                        q.appendleft((x1,y1,cost2,rem))
        return -1 if cost[m-1][n-1] == float('inf') else cost[m-1][n-1]
                
    def shortestPath(self, grid, k):
        \"\"\"
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        \"\"\"
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def getNei(x,y):
            for dx,dy in dirs:
                if 0<=x+dx<m and 0<=y+dy<n:
                    yield x+dx,y+dy,grid[x+dx][y+dy]
                
        m,n,maxmn = len(grid),len(grid[0]), 40*40
        costs = [[maxmn]*n for _ in range(m)]
        costs[0][0] = 0
        bfs = collections.deque([(0,0,0,k)])
        while bfs:
            x,y,cost,clears = bfs.popleft()            
            for xn,yn,blocked in getNei(x,y):
                newcost = cost+1
                newclears = clears-blocked
                if newclears >= 0 and newcost < costs[xn][yn]:
                    costs[xn][yn] = newcost
                    if blocked:
                        bfs.append((xn,yn,newcost,newclears))
                    else:
                        bfs.appendleft((xn,yn,newcost,newclears))
        return -1 if costs[m-1][n-1] == maxmn else costs[m-1][n-1]
            
