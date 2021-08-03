class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [n * [float(\"inf\")] for _ in range(n)]
        
        for a, b, w in edges:
            g[a][b] = g[b][a] = w
            
        # Floyd-Warshall complexity: O(n**3) 
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        
        res = -1
        resum = float(\"inf\")
        
        for i in range(n):
            
            isum = 0
            for j in range(n):
                if j != i and g[i][j] <= distanceThreshold:
                    isum += 1
            
            if isum <= resum:
                resum = isum
                res = i
        
        return res
