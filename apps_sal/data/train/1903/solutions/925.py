import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        hq, d, s = [(0, 0)], [1] * n, 0
        while hq:
            t, i = heapq.heappop(hq)
            if d[i]:
                s += t
                d[i] = 0
                for j in range(n):
                    if d[j]:
                        heapq.heappush(hq, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))
        return s
