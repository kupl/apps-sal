class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for u in range(n):
            dist[u][u] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > (d := dist[i][k] + dist[k][j]):
                        dist[i][j] = d
        ans = {}
        for i, a in enumerate(dist):
            for b in a:
                if(b <= distanceThreshold):
                    if(i in ans):
                        ans[i] += 1
                    else:
                        ans[i] = 1
        ans2 = 0
        minValue = 10000000

        for key, value in list(ans.items()):
            if(value <= minValue):
                minValue = value
                ans2 = key
        return ans2
