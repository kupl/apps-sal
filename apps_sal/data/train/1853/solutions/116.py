class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        table = [[float('inf') for j in range(n)] for i in range(n)]
        for i in range(n):
            table[i][i] = 0
            
        for v, u, w in edges:
            table[u][v] = w
            table[v][u] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    table[i][j] = min(table[i][j], table[i][k] + table[k][j])
                    
        count = [0] * n
        for i in range(n):
            for j in range(n):
                if table[i][j] <= distanceThreshold:
                    count[i] += 1
        
        #print(count)
        #print(table)
        m = min(count)                
        res = -1
        for i in range(n):
            if count[i] == m:
                res = i
                
        return res
