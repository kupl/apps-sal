import queue

def isOK(x, y, m, n):
    return x >=0 and y >=0 and x < m and y < n

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(start):
            island = []
            x, y = start
            visited[x][y] = True
            stack = [start]
            while stack:
                x, y = stack.pop()
                island.append((x, y))
                xRows = [0,0,-1,1]
                yCols = [-1, 1, 0,0]
                for i in range(4):
                    new_x = x + xRows[i]
                    new_y = y + yCols[i]
                    
                    if isOK(new_x, new_y, m, n) and not visited[new_x][new_y] and A[new_x][new_y]== 1:
                        stack.append((new_x, new_y))
                        visited[new_x][new_y] = True
                        
            return island
        
        islands = []
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and A[i][j] == 1:
                    island = dfs((i, j))
                    islands.append(island)
                    
                    
        source_island, target_island = islands
        
        print(source_island)
        print(target_island)
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def bfs(source_island, target_island, visited):
            q = queue.Queue()
            for start in source_island:
                x,y = start
                q.put((x, y, 0))
                
            while q.qsize() > 0:
                u = q.get()
                x, y, w = u
                xRows = [-1, 1, 0, 0]
                yCols = [0, 0, -1, 1]
                for i in range(4):
                    new_x = x + xRows[i]
                    new_y = y + yCols[i]
                    if isOK(new_x, new_y, m, n) and not visited[new_x][new_y]:
                        if (new_x, new_y) in target_island:
                            return w
                        
                        visited[new_x][new_y] = True
                        q.put((new_x, new_y, w + 1))
        # Time Complexity O(V + E)
        return bfs(source_island, target_island, visited)
                        
                    
        
                    
        
        
       
            
            
            
            
            
            
            
            
            
            
            
            

