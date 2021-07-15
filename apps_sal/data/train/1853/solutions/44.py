class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], limit: int) -> int:
        dist = [[float(\"inf\")]*n for _ in range(n)]
        for n1, n2, w in edges:
            dist[n1][n2] = w
            dist[n2][n1] = w
        
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        
        ans = {sum(dist[i][j] <= limit for j in range(n)):i for i in range(n)}
        return ans[min(ans)]
                            
            
