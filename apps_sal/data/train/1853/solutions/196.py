class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dists = [[distanceThreshold + 1 for i in range(n)] for j in range(n)]
        for s, e, w in edges:
            dists[s][e] = w
            dists[e][s] = w

        for i in range(n):
            dists[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dists[i][k] + dists[k][j] > distanceThreshold:
                        continue
                    elif dists[i][j] is None:
                        dists[i][j] = dists[i][k] + dists[k][j]
                    elif dists[i][k] + dists[k][j] < dists[i][j]:
                        dists[i][j] = dists[i][k] + dists[k][j]

        mn = n
        city = None
        for i in range(n):
            cnt = len([j for j in dists[i] if j <= distanceThreshold])
            if cnt <= mn:
                mn = cnt
                city = i
        return city
