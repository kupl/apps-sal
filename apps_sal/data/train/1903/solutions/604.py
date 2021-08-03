from heapq import heappush, heappop


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points.sort()
        visited = set()
        n = len(points)
        cnt = 0
        q = []

        heappush(q, (0, 0))
        while len(q):
            weight, source = heappop(q)
            if source in visited:
                continue
            cnt += weight
            visited.add(source)

            for i in range(n):
                if i not in visited:
                    weight = abs(points[i][0] - points[source][0]) + abs(points[i][1] - points[source][1])
                    heappush(q, (weight, i))

        return cnt
