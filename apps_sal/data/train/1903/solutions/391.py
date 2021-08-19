class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dsu = list(range(N))

        def find(i):
            if dsu[i] != i:
                dsu[i] = find(dsu[i])
            return dsu[i]

        def union(i, j):
            dsu[find(j)] = find(i)
        pq = []
        cost = 0
        for i in range(N):
            for j in range(i + 1, N):
                (i_x, i_y) = points[i]
                (j_x, j_y) = points[j]
                c = abs(i_x - j_x) + abs(i_y - j_y)
                pq.append((c, i, j))
        pq.sort(key=lambda x: x[0], reverse=True)
        while pq:
            (c, i, j) = pq.pop()
            (fi, fj) = (find(i), find(j))
            if fi == fj:
                continue
            cost += c
            dsu[fj] = fi
        return cost
