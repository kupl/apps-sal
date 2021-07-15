class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dirs(V, M, N):
            res = []            
            if V[0] > 0:
                res.append((V[0]-1, V[1]))
            if V[0] < M-1:
                res.append((V[0]+1, V[1]))
            if V[1] > 0:
                res.append((V[0], V[1]-1))
            if V[1] < N-1:
                res.append((V[0], V[1]+1))                
            return res

        
        
        def bfs(grid):
            q = []
            for j in I[0]: 
                level[j] = 0 
                q.append(j)
                visited.add(j) 
                        
            while q: 
                v = q.pop(0)                
                for neighbor in dirs(v, len(grid), len(grid[0])):
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
                        if neighbor in level: 
                            level[neighbor] = min(level[neighbor],level[v] + 1)
                        else:
                            level[neighbor] = level[v] + 1

                        
            return                         

                        
        def dfs(grid, i,j, m, n, S): 
            S.add((i,j)) 
            vis.add((i,j)) 
            
            for neighbor in dirs((i,j),m,n): 
                if neighbor not in vis and grid[neighbor[0]][neighbor[1]] == 1: 
                    dfs(grid, neighbor[0], neighbor[1], m, n, S)
#             if (i<(m-1)) and ((i+1,j) not in vis) and (grid[i+1][j] == 1): 
#                 dfs(grid, i+1, j, m, n, S)
                
#             if (i>0) and ((i-1,j) not in vis) and (grid[i-1][j] == 1):
#                 dfs(grid, i-1, j, m, n, S)
                                
#             if (j<(n-1)) and ((i,j+1) not in vis) and (grid[i][j+1] == 1):
#                 dfs(grid, i, j+1, m, n, S)
                                
#             if (j>0) and ((i,j-1) not in vis) and (grid[i][j-1] == 1):
#                 dfs(grid, i, j-1, m, n, S)                            
            return 
        
        M, N = len(A), len(A[0])
        I = []                
        vis = set()
        
        for i in range(M):
            for j in range(N): 
                if ((i,j) not in vis) and (A[i][j] == 1): 
                    s = set()
                    dfs(A,i,j,M,N,s)
                    I.append(s)
        
        # print(len(I[0]), len(I[1]))
        
        level = {}
        visited = set()
        bfs(A)
        
        # print(level)
        # print(d) 
        
        return min([level[j] for j in I[1]])-1
