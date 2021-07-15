MAX = 1601
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], K: int) -> int:
        m,n = len(grid), len(grid[0])
        #dp = [[{} for c in range(n)] for r in range(m)]
        maxK = [[-1]*n for _ in range(m)]
        
        q = deque([(0,0,0,K)])
        
        while q:
            i,j,d,k = q.popleft()
            if i==m-1 and j==n-1: 
                return d
            if k <= maxK[i][j]:
                continue
            maxK[i][j] = max(maxK[i][j], k)
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<m and 0<=y<n and k-grid[x][y]>=0:
                    q.append((x,y,d+1,k-grid[x][y]))
        
        return -1
