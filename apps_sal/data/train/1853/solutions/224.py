class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        dist = [[inf] * n for _ in range(n)]
        for (f, t, c) in edges:
            dist[f][t] = min(dist[f][t], c)
            dist[t][f] = min(dist[t][f], c)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        arr = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i == j or dist[i][j] > dt:
                    continue
                cnt += 1
            arr.append((cnt, -i))
        arr.sort()
        return -arr[0][1]
