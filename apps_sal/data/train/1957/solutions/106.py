from collections import defaultdict, deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def getNei(x,y):
            for dx,dy in dirs:
                xn,yn = x+dx,y+dy
                if 0<=xn<M and 0<=yn<N:
                    yield xn,yn
                
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        M, N = len(grid), len(grid[0])
        visited = [[[None]*(k+1) for _ in range(N)] for _ in range(M)]
        
        # visited[0][0][k] = True
        
        queue = deque([(0,0,k,0)])
        
        while queue:
            i, j, kk, cost = queue.popleft()
            
            if i==M-1 and j==N-1:
                return cost
            
            if visited[i][j][kk]:
                continue
            visited[i][j][kk] = True
            
            for x, y in getNei(i, j):
                if grid[x][y] == 1:
                    if kk > 0:
                        queue.append((x, y, kk-1, cost+1))
                else:
                    queue.append((x, y, kk, cost+1))
        
        return -1
