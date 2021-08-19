class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from heapq import heappush, heappop
        n = len(points)
        h = {i: {} for i in range(n)}
        visited = [False] * n
        for p1 in range(n):
            for p2 in range(n):
                if p1 == p2:
                    continue
                d = abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
                h[p1][p2] = d
                h[p2][p1] = d
        total = 0
        ans = 0
        queue = [(0, 0)]
        while total < n:
            (d, node) = heappop(queue)
            if visited[node]:
                continue
            total += 1
            ans += d
            visited[node] = True
            for item in h[node]:
                if not visited[item]:
                    heappush(queue, (h[node][item], item))
        return ans
