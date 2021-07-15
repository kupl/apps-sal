class Solution(object):
          
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
                
        m,n,maxmn = len(grid),len(grid[0]), float('inf')
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
            
