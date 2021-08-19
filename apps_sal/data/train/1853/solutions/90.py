class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        for (s, e, w) in edges:
            dp[s][e] = w
            dp[e][s] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] != sys.maxsize and dp[j][k] != sys.maxsize:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        result = [0 for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if dp[i][j] <= distanceThreshold:
                    result[i] += 1
                    result[j] += 1
        return min([(i, val) for (i, val) in enumerate(result)], key=lambda x: (x[1], -x[0]))[0]
