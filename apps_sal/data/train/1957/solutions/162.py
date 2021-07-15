from collections import defaultdict, deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def getNei(x,y):
            for dx,dy in dirs:
                xn,yn = x+dx,y+dy
                if 0<=xn<m and 0<=yn<n:
                    yield xn,yn,grid[xn][yn]
                
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
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
                        bfs.append((xn,yn,newcost,newclears)) # dfs stack
                    else:
                        bfs.appendleft((xn,yn,newcost,newclears)) # bfs queue
        return -1 if costs[m-1][n-1] == maxmn else costs[m-1][n-1]
