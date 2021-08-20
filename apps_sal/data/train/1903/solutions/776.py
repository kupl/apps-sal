class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        visited = [False] * len(points)
        heap = [(0, 0)]
        res = 0
        while heap:
            (dist, node) = heapq.heappop(heap)
            if not visited[node]:
                res += dist
                visited[node] = True
                for neighbor in range(len(points)):
                    if not visited[neighbor]:
                        heapq.heappush(heap, (sum([abs(points[node][i] - points[neighbor][i]) for i in range(2)]), neighbor))
        return res
