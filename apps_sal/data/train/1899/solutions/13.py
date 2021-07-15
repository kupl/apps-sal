class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        r, c = -1, -1
        
        for i, row in enumerate(A):
            for j, val in enumerate(row):
                if val == 1:
                    r = i
                    c = j
                    break
        
        if r == -1 or c == -1:
            return -1
        
        
        nei = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(A, i, j, q):
            q.append((i, j, 0))
            A[i][j] = 2
            
            for dx, dy in nei:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 1:
                    dfs(A, nx, ny, q)
                    
            return
        
        q = []
        dfs(A, r, c, q)
        
        while q:
            cx, cy, dis = q.pop(0)
            
            for dx, dy in nei:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if A[nx][ny] == 1:
                        return dis
                    
                    if A[nx][ny] == 0:
                        q.append((nx, ny, dis+1))
                        A[nx][ny] = 2
                        
        return -1
                

