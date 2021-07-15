import itertools as it


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = float(\"inf\")
        dp = [[inf] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
        
        for a, b, w in edges:
            dp[a][b] = min(dp[a][b], w)
            dp[b][a] = min(dp[b][a], w)
            
        for k, j , i in it.permutations(range(n), 3):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            dp[j][i] = dp[i][j]
            
        out = min([(sum(1 for r in row if r <= distanceThreshold), -i) for i, row in enumerate(dp)])
        
        return -out[1]
        
