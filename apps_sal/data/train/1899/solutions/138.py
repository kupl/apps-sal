class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        m = len(A)
        n = len(A[0])
        found = 0
        queue = []
        
        def dfs(a, b):
            queue.append((a, b))
            A[a][b] = -1
            for x, y in (a+1, b), (a-1, b), (a, b+1), (a, b-1):
                if 0<=x< m and 0<=y<n and A[x][y] == 1:
                    dfs(x, y)
        
        
        for i in range(m):
            if found: 
                break
            for j in range(n):
                if A[i][j] == 1:
                    found = 1
                    dfs(i, j)
                    break
        step = 0
        while queue:
            new_queue = []
            for x, y in queue:
                for _x, _y in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if 0<=_x< m and 0<=_y<n:
                        if A[_x][_y] == 1:
                            return step
                        elif not A[_x][_y]:
                            A[_x][_y] = -1
                            new_queue.append((_x, _y))
            step += 1
            queue = new_queue
        return -1
                    
                        
                
            
            
        

