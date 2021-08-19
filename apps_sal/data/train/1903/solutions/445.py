class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        heap = []
        visited = set()
        res = 0
        cur = 0
        visited.add(0)
        while len(visited) != len(points):
            for i in range(len(points)):
                if cur == i:
                    continue
                heapq.heappush(heap, (abs(points[i][0] - points[cur][0]) + abs(points[i][1] - points[cur][1]), i))
            while True:
                (val, nxt) = heapq.heappop(heap)
                if nxt not in visited:
                    visited.add(nxt)
                    res += val
                    cur = nxt
                    break
        return res
