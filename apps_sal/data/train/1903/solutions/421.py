from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        P = [i for i in range(N)]
        E = []

        for u in range(N):
            x1, y1 = points[u]
            for v in range(u + 1, N):
                x2, y2 = points[v]

                E.append((u, v, abs(x1 - x2) + abs(y1 - y2)))

        E.sort(key=lambda edge: edge[2])

        def getParent(x):
            if x != P[x]:
                P[x] = getParent(P[x])

            return P[x]

        def join(u, v):
            pu = getParent(u)
            pv = getParent(v)

            if pu == pv:
                return False

            P[pu] = pv
            return True

        rs, count = 0, 0
        for u, v, w in E:
            if join(u, v):
                rs = rs + w
                count = count + 1

            if count == N:
                break

        return rs
