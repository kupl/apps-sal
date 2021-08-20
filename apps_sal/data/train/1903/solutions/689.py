class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        connected = 1
        result = 0
        heapq.heapify(edges)
        visited = set()
        i = 0
        while connected < n:
            connected += 1
            visited.add(i)
            a = points[i]
            for j in range(n):
                b = points[j]
                if j not in visited:
                    heapq.heappush(edges, (abs(a[0] - b[0]) + abs(a[1] - b[1]), j))
            while edges[0][1] in visited:
                heapq.heappop(edges)
            result += edges[0][0]
            i = heapq.heappop(edges)[1]
        return result
