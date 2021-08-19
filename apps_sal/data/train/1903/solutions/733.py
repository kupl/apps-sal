from heapq import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        if len(points) == 1:
            return result

        costHeap = []
        n = len(points)
        cur = 0
        def distance(p, np): return abs(p[0] - np[0]) + abs(p[1] - np[1])
        visited = [False for _ in range(n)]
        visited[0] = True
        size = 1

        for i in range(1, n):
            heappush(costHeap, [distance(points[0], points[i]), i])

        while costHeap:
            cost, nextStart = heappop(costHeap)
            # print(cur, nextStart, cost)
            if not visited[nextStart]:
                result += cost
                visited[nextStart] = True
                size += 1
                cur = nextStart
                for i in range(n):
                    heappush(costHeap, [distance(points[cur], points[i]), i])
                if size == n:
                    break

        return result
