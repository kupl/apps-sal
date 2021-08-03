class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])
        res, length, heap, visited = 0, len(points), [(0, 0)], set()
        while len(visited) < length:
            w, u = heapq.heappop(heap)
            if u not in visited:
                res += w
                visited.add(u)
                for v in range(length):
                    if v not in visited:
                        heapq.heappush(heap, (manhattan(points[u], points[v]), v))
        return res
