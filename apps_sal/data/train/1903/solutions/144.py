class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        seen = set()
        res = 0
        pq = [(0, 0, 0)]
        while len(seen) < n:
            w, u, v = heapq.heappop(pq)
            if u in seen and v in seen:
                continue
            res += w
            seen.add(u)
            seen.add(v)
            for i in range(n):
                if i != v and i not in seen:
                    heapq.heappush(pq, (manhattan(points[v], points[i]), v, i))
        return res
