class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 9999999
        dist = [[INF for j in range(n)] for i in range(n)]
        graph = [[] for i in range(n)]
        for e in edges:
            i = e[0]
            j = e[1]
            dist[i][j] = e[2]
            dist[j][i] = e[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        ans = -1
        mm = n
        for i in range(n):
            k = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    k += 1
            if k <= mm:
                mm = k
                ans = i
        return ans
