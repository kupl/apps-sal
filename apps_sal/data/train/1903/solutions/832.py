class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_weight(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])
        n = len(points)
        (visited, queue) = (set(), [(0, 0)])
        res = 0
        while queue:
            (weight, u) = heapq.heappop(queue)
            if u in visited:
                continue
            visited.add(u)
            res += weight
            for v in range(n):
                if v != u and v not in visited:
                    heapq.heappush(queue, (get_weight(points[u], points[v]), v))
        return res
