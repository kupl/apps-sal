class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float(\"inf\") for _ in range(n)] for _ in range(n)]
        
        for a in edges:
            graph[a[0]][a[1]] = a[2]
            graph[a[1]][a[0]] = a[2]
            
        for i in range(n):
            graph[i][i] = 0
            
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j]>graph[i][k]+graph[k][j]:
                        graph[i][j] = graph[i][k]+graph[k][j]
                        
        count = float(\"inf\")
        node = 0
        for i in range(n):
            a = graph[i]
            c = [x for x in a if x<=distanceThreshold]
            if len(c)<=count:
                count = len(c)
                node = i
                
        return node
            
                    
                    
                    
                
        
