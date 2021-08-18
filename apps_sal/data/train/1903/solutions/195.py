class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        n = len(points)
        par = [i for i in range(n)]
        sze = [1] * n

        def dist(pi: List[int], pj: List[int]) -> int:
            x, y = pi
            a, b = pj
            return abs(x - a) + abs(y - b)

        def find(i: int) -> int:
            if par[i] == i:
                return i
            return find(par[i])

        def union(i: int, j: int) -> int:
            par[i] = j
            sze[j] += sze[i]
            return sze[j]

        pq = []

        for i in range(n):
            pi = points[i]
            for j in range(i + 1, n):
                pj = points[j]
                heapq.heappush(pq, (dist(pi, pj), i, j))
        ok = set()
        total = 0
        usize = 0
        while usize < len(points):
            cost, i, j = heapq.heappop(pq)
            ri, rj = find(i), find(j)
            if ri != rj:
                usize = union(ri, rj)
                ok.add(i)
                ok.add(j)
                total += cost
        return total
