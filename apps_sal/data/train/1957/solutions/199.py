class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        R, C = len(grid), len(grid[0])
        if R == C == 1: return 0
        
        visited = [[[float('inf') for _ in range(C)] for _ in range(R)] for _ in range(k+1)]
        
        #visited[breaks remaining][row][column]
        
        q = [(0, k, 0, 0)]
        best = float('inf')
        
        while q:
            
            steps, b, r, c = heapq.heappop(q)
            
            if (b < 0) or (steps >= best):
                continue
            
            if steps >= visited[b][r][c]:
                continue
            if (r == R-1) and (c == C-1):
                best = min(best, steps)
            visited[b][r][c] = steps
            
            for i,j in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
                if (0 <= i < R) and (0 <= j < C) and (visited[b - grid[i][j]][i][j] > steps + 1):
                    heapq.heappush(q, (steps + 1, b - grid[i][j], i, j))
        
        res = min((visited[b][R-1][C-1] for b in range(k+1)))
        return res if (res != float('inf')) else -1
