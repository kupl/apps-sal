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

                
        def bfs(q):
            for j in q: 
                level[j] = 0 
                visited.add(j) 
                        
            while q: 
                v = q.pop(0)                
                for neighbor in dirs(v, len(A), len(A[0])):
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
                        if neighbor in level: 
                            level[neighbor] = min(level[neighbor],level[v] + 1)
                        else:
                            level[neighbor] = level[v] + 1                        
            return                         


        
        def dfs(grid, v, S): 
            S.add(v) 
            visited.add(v) 
            
            for neighbor in dirs(v,len(grid),len(grid[0])): 
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 1: 
                    dfs(grid, (neighbor[0], neighbor[1]), S)
                    
            return 
        
        I = []                
        visited = set()
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if ((i,j) not in visited) and (A[i][j] == 1): 
                    s = set()
                    dfs(A,(i,j),s)
                    I.append(s)
        
        # print(len(I[0]), len(I[1]))
        
        level = {}
        visited = set()
        bfs(list(I[0]))   
        
        return min([level[j] for j in I[1]])-1
