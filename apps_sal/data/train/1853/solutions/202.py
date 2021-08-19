class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        tb = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            tb[i][i] = 0

        for f, t, c in edges:
            tb[f][t] = tb[t][f] = c

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if tb[i][k] + tb[k][j] < tb[i][j]:
                        tb[i][j] = tb[i][k] + tb[k][j]

        i = -1
        c = n + 1
        for j in range(n):
            cc = sum(1 for x in tb[j] if x <= distanceThreshold)
            # print(j, cc)
            if cc <= c:
                i = j
                c = cc
        # print(tb)
        return i
