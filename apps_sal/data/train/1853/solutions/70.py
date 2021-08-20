class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[10001 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for (u, v, w) in edges:
            dp[u][v] = w
            dp[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        l = []
        smallest = 101
        for i in range(n):
            temp = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    temp += 1
            if temp < smallest:
                smallest = temp
                l = [i]
            elif temp == smallest:
                l.append(i)
        return l[-1]
